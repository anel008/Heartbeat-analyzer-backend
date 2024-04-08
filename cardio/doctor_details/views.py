from rest_framework import status, viewsets,filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .serializers import Ddetails_serializers
from .models import Doctor_profile
from django.contrib.auth.models import User
from rest_framework.generics import GenericAPIView,RetrieveUpdateAPIView,DestroyAPIView
from django_filters import rest_framework as filter
from rest_framework.views import APIView
from rest_framework import authentication, permissions







# Create your views here.



# ********* creating a doctor account ************* #

class d_create(GenericAPIView):
    serializer_class = Ddetails_serializers

    def post(self, request):
        # Ensure the authenticated user is retrieved properly
        user = request.user

        # Proceed only if the user is authenticated
        if user.is_authenticated:
            data = request.data
            serializer = self.get_serializer(data=data)
            if serializer.is_valid():
                validated_data = serializer.validated_data
                try:
                    # Creating a new instance of Doctor_profile
                    details = Doctor_profile.objects.create(
                        doctor_name=validated_data['doctor_name'],
                        license_no=validated_data['license_no'],
                        specialty=validated_data['specialty'],
                        email=validated_data['email'],
                        phone_number=validated_data['phone_number'],
                        bio=validated_data.get('bio', '')  # Use get() to avoid KeyError if bio is not provided
                    )
                    # Serializing the created instance and returning the response
                    response_serializer = Ddetails_serializers(details)
                    return Response(response_serializer.data, status=status.HTTP_201_CREATED)
                except Exception as e:
                    # Catch any other exception and return an internal server error
                    return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                # Return validation errors if the data is not valid
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Return an error if the user is not authenticated
            return Response({"error": "User not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)
        



# ********** fetching all the enterd details in doctor ************* #
        


class d_details(APIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request, *args, **kwargs):
        id=request.user.id
        qs=Doctor_profile.objects.filter(user_id=id)
        serializers=Ddetails_serializers(qs,many=True)
        return Response(data=serializers.data)



# ************** update the doctor profile *************** #

class Update_Doctor(RetrieveUpdateAPIView):
    serializer_class = Ddetails_serializers
    queryset = Doctor_profile.objects.all()

    def get_object(self):
        doctor_name = self.kwargs.get('doctor_name')  # Get the license_no from URL kwargs
        return Doctor_profile.objects.get(doctor_name=doctor_name)  # Retrieve the doctor based on the license_no

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# *************** delete function on Doctor ****************#
    
class Delete_Doctor(DestroyAPIView):
    serializer_class = Ddetails_serializers
    querry_set = Doctor_profile.objects.all()

    def get_object(self):
        doctor_name = self.kwargs.get('doctor_name')
        return Doctor_profile.objects.get(doctor_name = doctor_name)
    
    def delete (self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





# ************** searching doctor from lsit **************** #

class Doctor_postfilter(filter.FilterSet):
    search_feilds = filter.CharFilter(field_name="Doctor name", lookup_expr="iexact")


class Search_Doctors(viewsets.ModelViewSet):
    queryset = Doctor_profile.objects.all()
    serializer_class = Ddetails_serializers
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filter_class = Doctor_postfilter
    search_fields = ["doctor_name"]
    ordering_fields = "__all__"






# ************** Model prediction ***************** #


from rest_framework.parsers import FileUploadParser
import numpy as np 
from io import BytesIO
import librosa
import pickle

from django.conf import settings


class Forecast(APIView):
    file_parser_classes = [FileUploadParser]
    def extract_features(self,y, sr):
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
        spectral_rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)[0]
        zcr = librosa.feature.zero_crossing_rate(y)[0]
        rmse = librosa.feature.rms(y=y)[0]
        cepstrum = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)[0]
        D = librosa.stft(y)  # Compute the spectrogram
        spectral_spread = librosa.feature.spectral_bandwidth(y=y, sr=sr)[0]


        features = np.hstack((np.mean(mfccs, axis=1), 
                          np.mean(spectral_centroid), 
                          np.mean(spectral_rolloff), 
                          np.mean(zcr), 
                          np.mean(rmse),
                          np.mean(cepstrum),
                          np.mean(spectral_spread),))
        return features
    
    def load_model(self):
        with open('resources/model.pkl', 'rb') as file:
            model = pickle.load(file)

        with open("resources/label_encoder.pkl", 'rb') as file :
            label_encoder = pickle.load(file)

        return (model, label_encoder)
    def post(self, request):
            print("********************************************")
            print("Request = ", type(request.body))
            print("********************************************")
            
            audio_data = request.body
            file_buffer = BytesIO(audio_data)
            samples, sr = librosa.load(file_buffer)

            # Loading model
            model, label_encoder = self.load_model()

            input_feature_data = []
            for i in range(0, len(samples), (sr * 5)):
                input_feature_data.append(self.extract_features(samples[i:(i + (sr * 5))], sr))

            preds = model.predict(input_feature_data)
            aggregate_class_index = round(np.mean(preds))
            forecast = label_encoder.inverse_transform([aggregate_class_index])[0]

            return Response({'forecast': forecast}, status=status.HTTP_201_CREATED)