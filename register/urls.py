from os import name
import django
from django.shortcuts import render
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.register, name="register"),
    path("login/success/", views.loginsuccess, name="loginsuccess"),
    path("logout/success/", views.logoutsuccess, name="logoutsuccess"),
]