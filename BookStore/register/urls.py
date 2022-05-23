from django.urls import path, include
from register import views


urlpatterns = [
    path("", views.home, name='home'),
    path("Register", views.Register, name='register'),
    path("loginn", views.loginn, name='loginn'),
    path("profile", views.profile, name='profile'),
    path("adminlog",views.Aloginn),
    

]
