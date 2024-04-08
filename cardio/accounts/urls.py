from django.urls import path
from .views import PRegisterView,user_login, user_logout #,DRegisterView
from accounts import views


urlpatterns = [
    path('register',PRegisterView.as_view()),   # USER REGISTRATION
    #path('d',DRegisterView.as_view())
    path('login/', user_login),          # USER LOGIN 
    path('logout/', user_logout),        # USER LOGOUT
]
