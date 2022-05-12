from django.shortcuts import render,redirect
from django.contrib.auth.models import User

# Create your views here.

def Register(request):
    if request.method=='POST':
        Username=request.POST['User_name']
        email=request.POST['email']
        psw=request.POST['psw']
        first=request.POST['first']
        last=request.POST['last']

        user=User.objects.create_user(username=Username,email=email,password=psw,first_name=first,last_name=last)
        user.save()
        return redirect ("/register/home")
    return render(request,"register.html")

def home(request):
    return render(request,"home.html")