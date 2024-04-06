from django.contrib import admin
from .models import Patient_details,recordings



# Register your models here.
from .models import Patient_details
admin.site.register(Patient_details)
admin.site.register(recordings)
# admin.site.register(Doctor_details)
