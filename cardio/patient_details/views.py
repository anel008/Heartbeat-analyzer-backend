from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import pdetails_serializers
from .models import Patient_details
from rest_framework.generics import GenericAPIView

@api_view(['GET','POST'])
def getRoutes(request):
    routes = [
        {
            'endpoints' : '/patients/' ,
            'method' : 'GET' ,
            'body' : None,
            'description' :  ' Returns an array of patients',              



        },

    ]
    return Response(routes)


@api_view(['GET'])
def  p_details(request):
    details = Patient_details.objects.all()
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