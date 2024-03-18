from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length = 70, min_length = 8, write_only = True)
    email = serializers.EmailField(max_length = 100, min_length = 8)
    first_name = serializers.CharField(max_length = 100, min_length = 2)
    last_name = serializers.CharField(max_length = 100, min_length = 2)
    adhar_no = serializers.IntegerField(max_value = 999999999999)

    class Meta :
        model = User
        fields = ['username','first_name','last_name','adhar_no','email','password']


    def validate(self, attrs):
        email = attrs.get('email','')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': ['email is already in use']})
        return super().validate(attrs)
    def create(self, validated_data):
        return User.objects.create_user(validated_data)