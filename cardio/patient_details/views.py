
from rest_framework.response import Response
from .serializers import pdetails_serializers
from .models import Patient_details
from rest_framework.generics import GenericAPIView,RetrieveUpdateAPIView,DestroyAPIView
from django_filters import rest_framework as filter
from rest_framework import status, viewsets,filters
from django_filters.rest_framework import DjangoFilterBackend



# fetching the patient datas from the data base
class p_details(GenericAPIView):
    serializer_class = pdetails_serializers
    queryset = Patient_details.objects.all()

    def get(self,request):    
        details = self.get_queryset()    
        serialzers = pdetails_serializers(details,many = True)
        return Response(serialzers.data)



#@api_view(['GET'])
#def  p_details(request,pk):
#    details = Patient_details.objects.get(id = pk)
#   serializers = pdetails_serializers(details,many = False)
#    return Response(serializers.data)




class p_create(GenericAPIView):
    serializer_class = pdetails_serializers

    def post(self, request):
        data = request.data

        details = Patient_details.objects.create(
            name = data['name'],
            dob = data['dob'],
            phone_number = ['phone_number'],
            age = ['age'],
            weight = ['weight'],
            height = ['height'],
            sex = ['sex'],
            hyper_tension_bp = ['hyper_tension_bp'],
            chest_pain =['chest_pain'], 
            palpitation = ['palpitation'],
            surgery = ['surgery'],
            any_other =['any_other'],
        )
        serializer = pdetails_serializers(details)
        return Response(serializer.data)
    

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
    

# Delete patient list

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
    


# searching patient list 

class Patient_postfilter(filter.FilterSet):
    search_feilds = filter.CharFilter(field_name = "patient name", lookup_expr="iexact")


class Search_Patient(viewsets.ModelViewSet):
    serializer_class = pdetails_serializers
    queryset = Patient_details.objects.all()
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filter_class = Patient_postfilter
    search_fields = ["name"]
    ordering_fields = "__all__"
