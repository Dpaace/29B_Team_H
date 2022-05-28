from django.test import TestCase
from django.urls import reverse,resolve
from django.test import Client, SimpleTestCase, TestCase
from register.views import Bedit, Bdelete, contact

# Create your tests here.
class TestUrls(SimpleTestCase):
    def test_case_edit_url(self):
        url=reverse("edit", args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func,Bedit)

    def test_case_delete_url(self):
        url=reverse("delete", args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func,Bdelete)
    
    def test_case_contact_url(self):
        url=reverse("contact")
        print(resolve(url))
        self.assertEquals(resolve(url).func,contact)

# Test Cases for views
class TestViews(TestCase):
    def setUp(self):
        self.client=Client()
    
    def test_contact_views(self):
        response=self.client.get(reverse('contact'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'User/contact_us.html')