from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('user/register', views.user_create),
    path('user/login', views.login),
    path('log_out', views.log_out)
]
