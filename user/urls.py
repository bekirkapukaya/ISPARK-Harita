from django.contrib import admin
from django.urls import path
from . import views
app_name = "user"

urlpatterns = [
    path('', views.loginUser, name="login"),
    path('register', views.registerUser, name="register"),
    path('logout', views.logout, name="logout")
]
