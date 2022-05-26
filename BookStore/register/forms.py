from dataclasses import fields
from django import forms
from .models import AddBook



class add_book(forms.ModelForm):
    class Meta:
        model = AddBook
        fields = ("__all__")


class update_book(forms.ModelForm):
    class Meta:
        model = AddBook
        fields = ("__all__")