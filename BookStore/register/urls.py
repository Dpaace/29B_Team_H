from django.urls import path, include
from register import views


urlpatterns = [
    path("", views.home, name='home'),

    path("Register", views.Register, name='register'),
    path("loginn", views.loginn, name='loginn'),
    path("dash", views.maindash, name='dash'),
    path("profile", views.profile, name='profile'),
    path("logout", views.logout_page, name='logout'),


    # Important Function Defined
    path('afterlogin', views.afterlogin_view, name='afterlogin'),

    # path("adminlog", views.Aloginn, name='adminlog'),
    path("admindash", views.adminDashboard, name='admindash'),
    path("addbook", views.addbooks, name='addbook'),
    
    
    path("mybook", views.mybook),
    path("profile_setting", views.psetting),
    path("about", views.about),
    
    path("edit/<int:p_id>", views.Bedit),
    path("delete/<int:p_id>", views.Bdelete),
    path("contact", views.contact),
    path("bookdesc/<slug>", views.viewbook),
    path("favourite/<int:id>", views.fav_post),
    path("favourite_list", views.favourite_list),
    path("contact", views.contact),
    path('searched', views.srch),
    path("delacc/<int:id>", views.acc_del),
    path('blogs',views.blog),
    path('fiction',views.fiction),
    path('nonfiction', views.nonfiction),
    path('customers',views.customers),
    path("cdelete/<int:p_id>",views.cdelete),

    #add to cart
    path('update_item/',views.updateItem, name='update_item')
   

]
