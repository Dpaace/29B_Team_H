from django.urls import path,include
from register import views


urlpatterns =[
    path("",views.Register),
     path("home",views.home),
   
]