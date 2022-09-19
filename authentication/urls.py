from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.login, name="login"),
    path('signout', views.signout, name="signout"),
    path('caregiver_form', views.caregiver_form, name="caregiver_form"),
    path('clients-admin', views.clients_admin, name="clients-admin"),
    path('caregivers-admin', views.caregivers_admin, name="caregivers-admin"),
    path('users/approve/<int:id>', views.activateUser),
]