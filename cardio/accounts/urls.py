from django.urls import path
from .views import PRegisterView #,DRegisterView
from accounts import views

urlpatterns = [
    path('p',PRegisterView.as_view()),
    # path('d',DRegisterView.as_view())
    
]
