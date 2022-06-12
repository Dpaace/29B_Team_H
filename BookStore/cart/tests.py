from django.test import TestCase
from django.urls import reverse,resolve
from django.test import Client, SimpleTestCase, TestCase
from cart.views import cart, updateItem, checkout, processOrder, remove_order, delete_order

# Create your tests here.
class TestUrls(SimpleTestCase):
    def test_case_cart_url(self):
        url=reverse("cart")
        print(resolve(url))
        self.assertEquals(resolve(url).func,cart)

    def test_case_update_item_url(self):
        url=reverse("update_item")
        print(resolve(url))
        self.assertEquals(resolve(url).func,updateItem)

    def test_case_checkout_url(self):
        url=reverse("checkout")
        print(resolve(url))
        self.assertEquals(resolve(url).func,checkout)

    def test_case_process_order_url(self):
        url=reverse("process_order")
        print(resolve(url))
        self.assertEquals(resolve(url).func,processOrder)

    def test_case_remove_order_url(self):
        url=reverse("remove_order", args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func,remove_order)

    def test_case_delete_order_url(self):
        url=reverse("delete_order", args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func,delete_order)

