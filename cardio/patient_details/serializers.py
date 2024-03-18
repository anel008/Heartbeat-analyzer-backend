from rest_framework.serializers import ModelSerializer
from .models import Patient_details

class pdetails_serializers(ModelSerializer):
    class Meta:
        model = Patient_details
        fields = '__all__'

