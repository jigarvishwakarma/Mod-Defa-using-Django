from django.contrib import admin
from django.urls import path
from . import views

app_name ='accounts'

urlpatterns = [
    path('login/',views.login_app,name='login'),
    path('register/',views.register_app,name='register'),
    path('logout/',views.logout_app,name='logout'),
]