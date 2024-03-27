from django.urls import path
from .views import d_create,d_details,p_details,Search_Patient #,p_create #,DoctorUpdateDelete,Search_Doctors
from patient_details.views import p_create



urlpatterns = [
    
    path('dc',d_create.as_view()),#doctor create
    path('dd',d_details.as_view()),#doctor details
    # path('<int:pk>',DoctorUpdateDelete.as_view())
    path('pd',p_details.as_view()),#patient detail view
    path('pc',p_create.as_view()),   #patient create
    #path('Dsearch',Search_Doctors.as_view({'get':'list'})),
    path('Psearch',Search_Patient.as_view({'get':'list'}))

]
