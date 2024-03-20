from django.urls import path
from .views import d_create,d_details

urlpatterns = [
    
    path('d',d_create.as_view()),
    path('vd',d_details.as_view())

]
