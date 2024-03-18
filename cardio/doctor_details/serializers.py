from rest_framework.serializers import ModelSerializer
from .models import Doctor_details

class Ddetails_serializers(ModelSerializer):
    class Meta :
        model = Doctor_details
        fields = '__all__'