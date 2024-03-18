from django.db import models

# Create your models here.

class Patient_details(models.Model):
    age = models.PositiveIntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)

    CHOICES = [
        ('1', 'yes'),
        ('0', 'no'),
    ]
    
    hyper_tension_bp = models.CharField( max_length=50,choices=CHOICES)
    chest_pain = models.CharField( max_length=50,choices=CHOICES)
    palpitation = models.CharField( max_length=50,choices=CHOICES)
    surgery = models.CharField( max_length=50,choices=CHOICES)
    any_other = models.TextField(max_length = 50) 

# class Doctor_details(models.Model):
#     doctor_name = models.CharField(max_length=50)
#     description = models.TextField(max_length = 200)
#     health_condition = models.TextField(max_length=100)
