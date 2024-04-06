
from rest_framework.response import Response
from .serializers import pdetails_serializers,recording_serializers
from .models import Patient_details
from rest_framework.generics import GenericAPIView,RetrieveUpdateAPIView,DestroyAPIView
from rest_framework.views import APIView
from django_filters import rest_framework as filter
from rest_framework import status, viewsets,filters,authentication, permissions
from django_filters.rest_framework import DjangoFilterBackend



# *************** fetching the patient datas from the data base ***************** #



from rest_framework.views import APIView


class p_details(APIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request, *args, **kwargs):
        id=request.user.id
        qs=Patient_details.objects.filter(user_id=id)
        serializers=pdetails_serializers(qs,many=True)
        return Response(data=serializers.data)







# class p_details(GenericAPIView):
#     serializer_class = pdetails_serializers
#     queryset = Patient_details.objects.all()

#     def get(self,request):    
#         details = self.get_queryset()    
#         serialzers = pdetails_serializers(details,many = True)
#         print("#########################")
#         print("User id ", request.user)
#         print("#########################")
#         return Response(serialzers.data)



#@api_view(['GET'])
#def  p_details(request,pk):
#    details = Patient_details.objects.get(id = pk)
#   serializers = pdetails_serializers(details,many = False)
#    return Response(serializers.data)



# ********* creating a patient deatails ************* #
# from rest_framework import authentication, permissions


class p_create(GenericAPIView):
    # authentication_classes=[authentication.BasicAuthentication]
    # permission_classes=[permissions.IsAuthenticated]


    serializer_class = pdetails_serializers

    def post(self, request):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        
        # Extracting data from the serializer
        validated_data = serializer.validated_data
        
        # Creating a new instance of Patient_details
        details = Patient_details.objects.create(
            name=validated_data['name'],
            dob=validated_data['dob'],
            phone_number=validated_data['phone_number'],
            age=validated_data['age'],
            weight=validated_data['weight'],
            height=validated_data['height'],
            sex=validated_data['sex'],
            hyper_tension_bp=validated_data['hyper_tension_bp'],
            chest_pain=validated_data['chest_pain'], 
            palpitation=validated_data['palpitation'],
            surgery=validated_data['surgery'],
            any_other=validated_data['any_other'],
            user_id=request.user  # Assign the authenticated user directly
        )   

        # Serializing the created instance and returning the response
        response_serializer = self.get_serializer(details)
        return Response(response_serializer.data)






# ************** update the patient details *************** #

class Update_Patient(RetrieveUpdateAPIView):
    serializer_class = pdetails_serializers
    queryset = Patient_details.objects.all()

    def get_object(self):
        name = self.kwargs.get('name')
        return Patient_details.objects.get(name= name)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data = request.data, partial = True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# ************* Delete patient list ***************** #

class Delete_patient(DestroyAPIView):
    serializer_class = pdetails_serializers  # Not required for delete operation
    queryset = Patient_details.objects.all() 

    def get_object(self):
        name = self.kwargs.get('name') 
        return Patient_details.objects.get(name=name)  # Retrieve the patient based on the name

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


# ************** searching patient list **************** #

class Patient_postfilter(filter.FilterSet):
    search_feilds = filter.CharFilter(field_name = "patient name", lookup_expr="iexact")


class Search_Patient(viewsets.ModelViewSet):
    serializer_class = pdetails_serializers
    queryset = Patient_details.objects.all()
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filter_class = Patient_postfilter
    search_fields = ["name"]
    ordering_fields = "__all__"


# ************** RECORDING *************** #

class recordings(APIView):
    serializer_class = recording_serializers

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()  # This will save the uploaded file to the record field
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)