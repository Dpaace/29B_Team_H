from dataclasses import fields
from django import forms
<<<<<<< HEAD
from .models import AddBook, Contact, UserP
from cart.models import *
=======
from .models import AddBook

>>>>>>> 95b8839843f97dc739f3b6ff9659038d3e5dd691


class add_book(forms.ModelForm):
    class Meta:
        model = AddBook
        fields = ("__all__")


<<<<<<< HEAD

class update_book(forms.ModelForm):
    class Meta:
        model = AddBook
        fields = ("__all__")


class contact_form(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("__all__")

class shipping_order(forms.ModelForm):
    class Meta:
        model =ShippingAddress
        fields = ['status']

class Update_form(forms.ModelForm):
    class Meta:
        model = UserP
=======
class update_book(forms.ModelForm):
    class Meta:
        model = AddBook
>>>>>>> 95b8839843f97dc739f3b6ff9659038d3e5dd691
        fields = ("__all__")