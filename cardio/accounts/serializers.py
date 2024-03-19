from rest_framework import serializers
from django.contrib.auth.models import User

#User registration 

class UserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length = 70, min_length = 8, write_only = True)
    email = serializers.EmailField(max_length = 100, min_length = 8)
    first_name = serializers.CharField(max_length = 100, min_length = 2)
    last_name = serializers.CharField(max_length = 100, min_length = 2)
    # adhar_no = serializers.IntegerField(max_value = 999999999999)

    class Meta :
        model = User
        fields = ['username','first_name','last_name','email','password']


    def validate(self, attrs):
        email = attrs.get('email','')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': ['email is already in use']})
        return super().validate(attrs)
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    

# Doctor registration

class Doctorserializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length = 100, min_length= 8, write_only = True)
    email = serializers.EmailField(max_length = 100, min_length = 8)
    first_name = serializers.CharField(max_length = 100, min_length = 2)
    last_name = serializers.CharField(max_length = 100, min_length = 2)
    Doctor_license_no = serializers.IntegerField()


    class Meta :
        model = User
        fields = ['first_name','last_name','username','email','Doctor_license_no','password']

        def validate(self, attrs):
            email = attrs.get('email','')
            if User.objects.filter(email=email).exists():
                raise serializers.ValidationError({'email' : ['email is already in use']})
            return super().validate(attrs)
        def create(self, validated_data):
            return User.objects.create_user(**validated_data)

        # def create(self, validated_data):
        #     doctor_license_no = validated_data.pop('Doctor_license_no')  # Remove Doctor_license_no from validated_data
        #     user = User.objects.create_user(**validated_data)  # Create the user without Doctor_license_no
        #     user.doctor_profile.Doctor_license_no = doctor_license_no  # Set Doctor_license_no separately
        #     user.save()  # Save the user
        #     return user      



