from django.urls import path, include
from register import views


urlpatterns = [
    path("", views.home, name='home'),
    path("Register", views.Register, name='register'),
    path("loginn", views.loginn, name='loginn'),
    path("profile", views.profile, name='profile'),
    path("adminlog",views.Aloginn),
    path("addbook",views.addbooks),
    path("admindash",views.adminDashboard),
    path("dash",views.maindash),
    path("mybook",views.mybook),
    path("profile_setting",views.psetting),
    path("about",views.about),
    path("logout",views.logout_page),
    path("edit/<int:p_id>",views.Bedit),
    path("delete/<int:p_id>",views.Bdelete),
    path("contact", views.contact),
]

