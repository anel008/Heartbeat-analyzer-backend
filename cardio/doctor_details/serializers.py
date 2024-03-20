from rest_framework.serializers import ModelSerializer
from .models import Doctor_profile

class Ddetails_serializers(ModelSerializer):
    class Meta :
        model = Doctor_profile
        fields = '__all__'