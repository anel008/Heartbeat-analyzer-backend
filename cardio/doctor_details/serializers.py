from rest_framework.serializers import ModelSerializer
from .models import Doctor_profile
from patient_details.models import Patient_details

class Ddetails_serializers(ModelSerializer):
    class Meta :
        model = Doctor_profile
        fields = '__all__'





