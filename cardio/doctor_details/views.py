from rest_framework import status, viewsets,filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .serializers import Ddetails_serializers
from .models import Doctor_profile
from rest_framework.generics import GenericAPIView,RetrieveUpdateAPIView,DestroyAPIView
from django_filters import rest_framework as filter







# Create your views here.



# ********* creating a doctor account ************* #

class d_create(GenericAPIView):
    serializer_class = Ddetails_serializers

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            try:
                details = Doctor_profile.objects.create(
                    doctor_name=validated_data['doctor_name'],
                    license_no=validated_data['license_no'],
                    specialty=validated_data['specialty'],
                    email=validated_data['email'],
                    phone_number=validated_data['phone_number'],
                    bio=validated_data.get('bio', '')  # Get bio if provided, otherwise default to empty string
                )
                serializer = Ddetails_serializers(details)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except KeyError as e:
                return Response({"error": f"Missing key in data: {e}"}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


# ********** fetching all the enterd details in doctor ************* #
        
class d_details(GenericAPIView):
    serializer_class = Ddetails_serializers
    queryset = Doctor_profile.objects.all()  # Define the queryset attribute

    def get(self, request):
        details = self.get_queryset()  # Retrieve queryset using get_queryset() method
        serializer = Ddetails_serializers(details, many=True)
        return Response(serializer.data)
    

# ************** update the doctor profile *************** #

class Update_Doctor(RetrieveUpdateAPIView):
    serializer_class = Ddetails_serializers
    queryset = Doctor_profile.objects.all()

    def get_object(self):
        license_no = self.kwargs.get('license_no')  # Get the license_no from URL kwargs
        return Doctor_profile.objects.get(license_no=license_no)  # Retrieve the doctor based on the license_no

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
        license_no = self.kwargs.get('license_no')
        return Doctor_profile.objects.get(license_no = license_no)
    
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


