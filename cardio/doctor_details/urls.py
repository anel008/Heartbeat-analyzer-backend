from django.urls import path
from .views import d_create,d_details #,p_create #,DoctorUpdateDelete,Search_Doctors
from patient_details.views import p_create,Search_Patient,p_details



urlpatterns = [
    
    path('dc',d_create.as_view()),#doctor create
    path('dd',d_details.as_view()),#doctor details
    path('pd',p_details.as_view()),#patient detail view
    path('pc',p_create.as_view()),   #patient create
    path('Psearch',Search_Patient.as_view({'get':'list'})) # patient search 

]
