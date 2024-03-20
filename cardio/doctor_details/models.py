from django.db import models

# Create your models here.
class Doctor_profile(models.Model):
    doctor_name = models.CharField(max_length=50, default='DOCTOR')
    license_no = models.CharField( max_length=50,default='XXXXX')
    specialty = models.CharField(max_length=100, default='XXXXX')
    email = models.EmailField(default='example@example.com')
    phone_number = models.CharField(max_length=20, default = 0)
    bio = models.TextField(blank=True)


