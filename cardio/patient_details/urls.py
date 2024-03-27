from django.urls import path
from .import views
from .views import p_create,p_details
from doctor_details.views import Search_Doctors

urlpatterns = [
    path('pd',p_details.as_view()),#patient detail view
    #path('p/<str:pk>/',views.p_details),
    # path('d',views.d_details)
    path('create',p_create.as_view()),
    path('Dsearch',Search_Doctors.as_view({'get':'list'})),
]