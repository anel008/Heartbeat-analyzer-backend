from django.urls import path
from .import views
from .views import p_create

urlpatterns = [
    path('', views.getRoutes),
    path('p',views.p_details),
    path('p/<str:pk>/',views.p_details),
    # path('d',views.d_details)
    path('create',p_create.as_view())
]