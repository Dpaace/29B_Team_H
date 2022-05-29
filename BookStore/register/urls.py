from django.urls import path, include
from register import views


urlpatterns = [
    path("", views.home, name='home'),
    path("Register", views.Register, name='register'),
    path("loginn", views.loginn, name='loginn'),
    path("profile", views.profile, name='profile'),
    path("adminlog", views.Aloginn),
    path("addbook", views.addbooks),
    path("admindash", views.adminDashboard),
    path("dash", views.maindash, name='dash'),
    path("mybook", views.mybook),
    path("profile_setting", views.psetting),
    path("about", views.about),
    path("logout", views.logout_page),
    path("edit/<int:p_id>", views.Bedit),
    path("delete/<int:p_id>", views.Bdelete),
    path("contact", views.contact),
    path("bookdesc", views.viewbook),
    path("favourite/<int:id>", views.fav_post),
    path("favourite_list", views.favourite_list),
    path("contact", views.contact),
    path('<slug:post>', views.post_detail),


]
