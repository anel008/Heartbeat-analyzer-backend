from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.



class Patient_details(models.Model):
    name = models.CharField(max_length=100, default='patient')
    dob = models.DateField(default=timezone.now)
    phone_number = models.IntegerField( default='0')
    age = models.IntegerField(default=0)  # Changed to IntegerField
    weight = models.IntegerField(default=0)  
    height = models.IntegerField(default=0)  

    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)

    YES_NO_CHOICES = [
        ('1', 'Yes'),
        ('0', 'No'),
    ]

    hyper_tension_bp = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='0')  # Default added
    chest_pain = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='0')  # Default added
    palpitation = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='0')  # Default added
    surgery = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='0')  # Default added
    any_other = models.TextField(max_length=50, default='')  # Default added

    user_id=models.ForeignKey(User,on_delete=models.CASCADE,null=True)






# class Patient_details(models.Model):
#     name = models.CharField(max_length = 100, default= 'patient')
#     dob = models.DateField(default=timezone.now)
#     phone_number = models.CharField(max_length = 12 , default = 0)
#     age = models.CharField(max_length = 200)
#     weight = models.CharField(max_length=5,)
#     height = models.CharField(max_length=5,)
#     SEX_CHOICES = [
#         ('M', 'Male'),
#         ('F', 'Female'),
#         ('O', 'Other'),
#     ]
#     sex = models.CharField(max_length=1, choices=SEX_CHOICES)

#     CHOICES = [
#         ('1', 'yes'),
#         ('0', 'no'),
#     ]
    
#     hyper_tension_bp = models.CharField( max_length=50,choices=CHOICES)
#     chest_pain = models.CharField( max_length=50,choices=CHOICES)
#     palpitation = models.CharField( max_length=50,choices=CHOICES)
#     surgery = models.CharField( max_length=50,choices=CHOICES)
#     any_other = models.TextField(max_length = 50) 
#     user_id=models.ForeignKey(User,on_delete=models.CASCADE,null=True)




# class Doctor_details(models.Model):
#     doctor_name = models.CharField(max_length=50)
#     description = models.TextField(max_length = 200)
#     health_condition = models.TextField(max_length=100)



class recordings(models.Model):
    patient = models.ForeignKey(Patient_details, on_delete=models.CASCADE,null=True)
    record = models.FileField(upload_to='recordfile')