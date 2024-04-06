from rest_framework.serializers import ModelSerializer
from .models import Patient_details,recordings
from rest_framework import serializers



class pdetails_serializers(ModelSerializer):
    any_other = serializers.CharField(max_length=50, allow_blank=True)
    class Meta:
        model = Patient_details
        fields = ['name','dob','phone_number','age','weight','height','sex','hyper_tension_bp','chest_pain','palpitation','surgery','any_other','user_id']

class recording_serializers(ModelSerializer):

    class Meta:
        model = recordings
        fields = '__all__'