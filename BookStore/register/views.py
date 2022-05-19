from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from register.forms import *

# Create your views here.
def home(request):
    return render(request, "home.html")

def addbooks(request):
    if request.method=="POST":
        form=add_book(request.POST, request.FILES)
        form.save()
        return redirect("",name='home')
    return render(request, "admin/Add_book.html")




def Register(request):
    if request.method == 'POST':
        Username = request.POST['user_name']
        email = request.POST['email']
        psw = request.POST['psw']
        first = request.POST['first']
        last = request.POST['last']

        user = User.objects.create_user(username=Username, email=email, password=psw, first_name=first, last_name=last)
        user.save()
        return redirect("home")
    return render(request, "signin/signin.html")


def loginn(request):
    if request.method == 'POST':
        customer_name = request.POST.get("user_name")
        customer_password = request.POST.get("psw")
        user = authenticate(request, username=customer_name, password=customer_password)
        if user is not None:
            login(request, user)
            print(request.user.username)
            return redirect("home")
    return render(request, "signin/signin.html")


def Aloginn(request):
    if request.method == 'POST':
        customer_name = request.POST.get("user_name")
        customer_password = request.POST.get("psw")
        
        print("admin")
        user = authenticate(request, username=customer_name, password=customer_password)
        if user is not None:
            login(request, user)
            print(request.user.username)
            return redirect("home")
    return render(request, "login.html")


def profile(request):
    return render(request, "User/profile.html")


def admindash(request):
    return render(request, "Admin/admindash.html")
