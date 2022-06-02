from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from register.forms import *
from register.models import AddBook
from django.contrib import messages
from django.template.loader import render_to_string
import os
from register.models import AddBook
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
# Create your views here.


def Register(request):
    if request.method == 'POST':
        print("register")
        Username = request.POST['user_name']
        email = request.POST['email']
        psw = request.POST['psw']
        first = request.POST['first']
        last = request.POST['last']

        user = User.objects.create_user(
            username=Username, email=email, password=psw, first_name=first, last_name=last)
        user.save()
        return redirect("home")
    return render(request, "signin/signin.html")


def loginn(request):
    if request.method == 'POST':
        customer_name = request.POST.get("user_name")
        customer_password = request.POST.get("psw")
        user = authenticate(request, username=customer_name,
                            password=customer_password)
        if user is not None:
            login(request, user)
            print(request.user.username)
            return redirect("/dash")
        else:
            print("not validate")
            messages.error(request, "Not Validate account ")
   
    return render(request, "signin/signin.html")


def logout_page(request):
    logout(request)
    request.session.clear()
    return render(request, "homepage.html")


def maindash(request):
    dash = AddBook.objects.raw("select * from addbook")
    fiction=AddBook.objects.filter(b_genre="Fiction")
    return render(request, "maindash.html", {'dash': dash,'fiction':fiction})

#genre tempalates
def fiction(request):
    dash = AddBook.objects.raw("select * from addbook")
    fiction=AddBook.objects.filter(b_genre="Fiction")
    return render(request, "genre/fiction.html", {'dash': dash,'fiction':fiction})

def nonfiction(request):
    dash = AddBook.objects.raw("select * from addbook")
    nonfiction=AddBook.objects.filter(b_genre="Nonfiction")
    return render(request, "genre/nonfiction.html", {'dash': dash,'nonfiction':nonfiction})



def home(request):
    return render(request, "homepage.html")


# ADMIn section
def Aloginn(request):
    if request.method == 'POST':
        customer_name = request.POST.get("user_name")
        customer_password = request.POST.get("psw")
        print("admin")
        user = authenticate(request, username=customer_name,
                            password=customer_password)
        if user is not None:
            login(request, user)
            print(request.user.username)
            return redirect("home")
    else:
        messages.error(request, "data has been updated ")
    return render(request, "Admin/ADlogin.html")


def adminDashboard(request):
    dash = AddBook.objects.raw("select * from addbook")
    return render(request, "Admin/admindash.html", {'dash': dash})


def addbooks(request):
    if request.method == "POST":
        form = add_book(request.POST, request.FILES)
        form.save()
        return redirect("/admindash")
    return render(request, "admin/Add_book.html")


def Bedit(request, p_id):
    books = AddBook.objects.get(book_id=p_id)

    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(books.b_pic) > 0:
                os.remove(books.b_pic.path)
            books.b_pic = request.FILES['b_pic']
        form = add_book(request.POST, instance=books)

        form.save()
        messages.success(request, "data has been updated ")
        return redirect("/admindash")
    return render(request, "Admin/update_book.html", {'books': books})


def viewbook(request, p_id):
    books = AddBook.objects.get(book_id=p_id)
    return render(request, "viewbook.html", {'books': books})


def Bdelete(request, p_id):
    books = AddBook.objects.get(book_id=p_id)
    books.delete()
    messages.success(request, "data has been deleted ")
    return redirect("/admindash")

# profile page


def profile(request):
    return render(request, "User/profile.html")


def mybook(request):
    return render(request, "User/mybooks.html")


def psetting(request):
    return render(request, "User/settings.html")


def about(request):
    return render(request, "User/about.html")


def contact(request):
    if request.method == "POST":
        form = contact_form(request.POST)
        form.save()
        return redirect("/dash")

    return render(request, "User/contact_us.html")

# bookmark
def post_detail(request, id, slug):
    post = get_object_or_404(AddBook, book_id=id, slug=slug)
    print("hh")
    is_favourite = False
    if post.favourite.filter(id=request.user.id).exists():
        is_favourite = True
    context = {
        'post': post,
        'is_favourite': is_favourite
    }

    return HttpResponseRedirect(request.META['HTTP_REFERER'], {'post': post, 'is_favourite': is_favourite})


def fav_post(request, id):
    post = get_object_or_404(AddBook, book_id=id)

    if post.favourite.filter(id=request.user.id).exists():
        post.favourite.remove(request.user)
        
    else:
        post.favourite.add(request.user)
    context = {
        'post': post,
        
    }

    return HttpResponseRedirect(request.META['HTTP_REFERER'], context)


def favourite_list(request):
    new = AddBook.newmanager.filter(favourite=request.user)
    return render(request, "User/fav_list.html", {'new': new})


#search bar
def srch(request):
    if request.method=="POST":
        searched=request.POST['searched']
        venues = AddBook.objects.filter(b_name__icontains=searched)
        dash = AddBook.objects.raw("select * from addbook")
        return render(request, "search.html",{'searched':searched,'venues':venues,'dash':dash})
    else:
        return render(request,'search.html')

def acc_del(request, id):
    user = User.objects.get(id = id)
    user.delete()
    messages.success(request, "your account has been deleted ")
    return redirect("/")

def blog(request):
    return render(request,'blogs.html')
