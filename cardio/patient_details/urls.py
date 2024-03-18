from django.urls import path
from .import views

urlpatterns = [
    path('', views.getRoutes),
    path('p',views.p_details),
    path('p/<str:pk>/',views.p_details),
    path('d',views.d_details)
]