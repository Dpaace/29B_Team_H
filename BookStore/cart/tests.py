from django.test import TestCase
from django.urls import reverse,resolve
from django.test import Client, SimpleTestCase, TestCase
from cart.views import Orderbook_details
from register.views import user_order, delivery_update, show_products

# Create your tests here.
class TestUrls(SimpleTestCase):
    def test_case_orderbook_url(self):
        url=reverse("orderbook_display", args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func,Orderbook_details)

    def test_case_uder_order_url(self):
        url=reverse("user_order")
        print(resolve(url))
        self.assertEquals(resolve(url).func,user_order)

    def test_case_delivery_update_url(self):
        url=reverse("delivery_update")
        print(resolve(url))
        self.assertEquals(resolve(url).func,delivery_update)

    def test_case_show_products_url(self):
        url=reverse("show_products")
        print(resolve(url))
        self.assertEquals(resolve(url).func,show_products)