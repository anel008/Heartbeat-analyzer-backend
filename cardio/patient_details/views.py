
from rest_framework.response import Response
from .serializers import pdetails_serializers
from .models import Patient_details
from doctor_details.models import Doctor_profile
from doctor_details.serializers import Ddetails_serializers
from rest_framework.generics import GenericAPIView
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
    


#searching doctor list
    

class Doctor_postfilter(filter.FilterSet):
    search_feilds = filter.CharFilter(field_name="Doctor name", lookup_expr="iexact")


class Search_Doctors(viewsets.ModelViewSet):
    queryset = Doctor_profile.objects.all()
    serializer_class = Ddetails_serializers
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filter_class = Doctor_postfilter
    search_fields = ["doctor_name"]
    ordering_fields = "__all__"