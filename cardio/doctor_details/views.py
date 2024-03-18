from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Ddetails_serializers
from .models import Doctor_details
# Create your views here.



@api_view(['GET'])
def d_details(request):
    details = Doctor_details.objects.all()
    serializers = Ddetails_serializers(details,many = True)
    return Response(serializers.data)