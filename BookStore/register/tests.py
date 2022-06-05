from django.test import TestCase
from django.urls import reverse,resolve
from django.test import Client, SimpleTestCase, TestCase
from register.views import customers, blog, srch, cdelete

# Create your tests here.
class TestUrls(SimpleTestCase):
    def test_case_customers_url(self):
        url=reverse("customers")
        print(resolve(url))
        self.assertEquals(resolve(url).func,customers)

    def test_case_blog_url(self):
        url=reverse("blogs")
        print(resolve(url))
        self.assertEquals(resolve(url).func,blog)
    
    def test_case_search_url(self):
        url=reverse("searched")
        print(resolve(url))
        self.assertEquals(resolve(url).func,srch)

    def test_case_cdelete_url(self):
        url=reverse("cdelete" , args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func,cdelete)

# Test Cases for views
class TestViews(TestCase):
    def setUp(self):
        self.client=Client()
    
    def test_customers_views(self):
        response=self.client.get(reverse('customers'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'Admin/customers.html')

    def test_blog_views(self):
        response=self.client.get(reverse('blogs'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'blogs.html')

    def test_search_views(self):
        response=self.client.get(reverse('searched'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'search.html')