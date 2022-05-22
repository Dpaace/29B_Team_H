from tkinter import N
from unicodedata import name
from django.urls import path, include
from register import views


urlpatterns = [
    path("", views.home, name='home'),
    path("Register", views.Register, name='register'),
    path("loginn", views.loginn, name='loginn'),
    path("profile", views.profile, name='profile'),
    path("adminlog",views.Aloginn, name='Aloginn'),
    path("addbook",views.addbooks, name='addbooks'),
    path("admindash",views.adminDashboard, name='adminDashboard'),
    path("dash",views.maindash, name='maindash'),
    path("mybook",views.mybook, name='mybook'),
    path("profile_setting",views.psetting, name='psetting'),
    path("about",views.about, name='about'),
    path("logout",views.logout_page, name='logout_page'),
]

