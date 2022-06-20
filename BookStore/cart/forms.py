from dataclasses import fields
from django import forms
from .models import ShippingAddress



class shipping(forms.ModelForm):
    class Meta:
        model =ShippingAddress
        fields = ("__all__")

# class shipping(forms.ModelForm):
#     class Meta:
#         model =ShippingAddress
#         fields = ("__all__")