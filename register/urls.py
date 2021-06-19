from os import name
import django
from django.db import reset_queries
from django.shortcuts import render
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.register, name="register"),
    path("accounts/profile/",views.userprofile, name="profile"),
    path("forgot-password/", views.change_password, name="reset_password"),
    path("accounts/change-password/", views.change_password, name="change password"),
]