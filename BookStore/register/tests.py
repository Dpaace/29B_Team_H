from django.test import TestCase
from django.urls import reverse,resolve
from django.test import Client, SimpleTestCase, TestCase
from register.views import home, Register, loginn, profile, Aloginn, addbooks, adminDashboard, maindash, mybook
from register.views import psetting, about, logout_page



# Create your tests here.
class TestUrls(SimpleTestCase):
    def test_case_home_url(self):
        url=reverse("home")
        print(resolve(url))
        self.assertEquals(resolve(url).func,home)

    def test_case_register_url(self):
        url=reverse("register")
        print(resolve(url))
        self.assertEquals(resolve(url).func,Register)
        
    def test_case_login_url(self):
        url=reverse("loginn")
        print(resolve(url))
        self.assertEquals(resolve(url).func,loginn)

    def test_case_profile_url(self):
        url=reverse("profile")
        print(resolve(url))
        self.assertEquals(resolve(url).func, profile)

    def test_case_admin_login_url(self):
        url=reverse("Aloginn")
        print(resolve(url))
        self.assertEquals(resolve(url).func, Aloginn)

    def test_case_addbooks_url(self):
        url=reverse("addbooks")
        print(resolve(url))
        self.assertEquals(resolve(url).func, addbooks)

    def test_case_adminDashboard_url(self):
        url=reverse("adminDashboard")
        print(resolve(url))
        self.assertEquals(resolve(url).func, adminDashboard)

    def test_case_maindash_url(self):
        url=reverse("maindash")
        print(resolve(url))
        self.assertEquals(resolve(url).func, maindash)

    def test_case_mybook_url(self):
        url=reverse("mybook")
        print(resolve(url))
        self.assertEquals(resolve(url).func, mybook)

    def test_case_psetting_url(self):
        url=reverse("psetting")
        print(resolve(url))
        self.assertEquals(resolve(url).func, psetting)

    def test_case_about_url(self):
        url=reverse("about")
        print(resolve(url))
        self.assertEquals(resolve(url).func, about)

    def test_case_logout_page_url(self):
        url=reverse("logout_page")
        print(resolve(url))
        self.assertEquals(resolve(url).func, logout_page)