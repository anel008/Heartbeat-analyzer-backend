from django.db import models

# Create your models here.
class Doctor_details(models.Model):
    doctor_name = models.CharField(max_length=50)
    description = models.TextField(max_length = 200)
    health_condition = models.TextField(max_length=100)