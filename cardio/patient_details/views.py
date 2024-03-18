from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import pdetails_serializers,Ddetails_serializers
from .models import Patient_details,Doctor_details

@api_view(['GET','POST'])
def getRoutes(request):
    routes = [
        {
            'endpoints' : '/notes/' ,
            'method' : 'GET' ,
            'body' : None,
            'description' :  ' Returns an array of notes',              



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

# @api_view(['GET'])
# def d_details(request):
#     details = Doctor_details.objects.all()
#     serializers = Ddetails_serializers(details,many = True)
#     return Response(serializers.data)
