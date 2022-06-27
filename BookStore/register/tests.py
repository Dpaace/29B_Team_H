from django.test import TestCase
from django.urls import reverse,resolve
from django.test import Client, SimpleTestCase, TestCase
from register.views import mybook, completeOrder

# Create your tests here.
class TestUrls(SimpleTestCase):
    def test_case_mybook_url(self):
        url=reverse("mybook")
        print(resolve(url))
        self.assertEquals(resolve(url).func,mybook)

    def test_case_completeOrder_url(self):
        url=reverse("completeOrder")
        print(resolve(url))
        self.assertEquals(resolve(url).func,completeOrder)

# Test Cases for views
class TestViews(TestCase):
    def setUp(self):
        self.client=Client()
    
    def test_mybook_views(self):
        response=self.client.get(reverse('mybook'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'User/mybooks.html')

    def test_completeOrder_views(self):
        response=self.client.get(reverse('completeOrder'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'Admin/completed_order.html')
