from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json

# Create your views here.
#start add to cart function
def cart(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items =order.orderitem_set.all()
    return render(request, "cart.html", {'items':items,'order':order})

def checkout(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items =order.orderitem_set.all()

    return render(request,'checkout.html',{'items':items,'order':order})

def updateItem(request):
    data = json.loads(request.body)
    productId=data['productId']
    action=data['action']

    print("Action:",action)
    print("productId:", productId)

    customer =request.user.customer
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

