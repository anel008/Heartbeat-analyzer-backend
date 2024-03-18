from rest_framework.serializers import ModelSerializer
from .models import Patient_details,Doctor_details

class pdetails_serializers(ModelSerializer):
    class Meta:
        model = Patient_details
        fields = '__all__'


class Ddetails_serializers(ModelSerializer):
    class Meta :
        model = Doctor_details
        fields = '__all__'