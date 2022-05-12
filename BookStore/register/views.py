from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


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

def loginn(request):
    if request.method=='POST':
        customer_name=request.POST.get("User_name")
        customer_password=request.POST.get("psw")        

        user = authenticate(request, username=customer_name,password=customer_password)
      
        if user is not None:
            login(request, user)
            print(request.user.username)
            return redirect ("/register/home")

        
    return render(request,"login.html")