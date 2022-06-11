from contextlib import nullcontext
from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import *
import json
import datetime
from .forms import *
# Create your views here.
#start add to cart function
def cart(request):
    customer = request.user
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items =order.orderitem_set.all()
    return render(request, "cart.html", {'items':items,'order':order})

def checkout(request):
    customer = request.user
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items =order.orderitem_set.all()
  
    if request.method == "POST":

        form = shipping(request.POST)
        transaction_id=datetime.datetime.now().timestamp()
        order.transaction_id=transaction_id
        if transaction_id != None:
            order.complete= True
            order.save()

        form.save()
        return redirect("/dash")
    

    return render(request,'checkout.html',{'items':items,'order':order})

def updateItem(request):
    data = json.loads(request.body)
    productId=data['productId']
    action=data['action']

    print("Action:",action)
    print("productId:", productId)

    customer =request.user
    product= AddBook.objects.get(book_id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created =OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity=(orderItem.quantity + 1)
    
    elif action == 'remove':
        orderItem.quantity=(orderItem.quantity - 1)
    
    orderItem.save()

    if orderItem.quantity <=0:
        orderItem.delete()
        
    return JsonResponse('responseData', safe=False)


def processOrder(request):
    transaction_id=datetime.datetime.now().timestamp()
    date=json.loads(request.body)

    customer=request.user
  
    return JsonResponse('paymennt sucessful', safe=False)


