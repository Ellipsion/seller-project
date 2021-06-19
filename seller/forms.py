from django import forms
from .models import *
from django.forms import ModelForm


class BankDetailsForm(ModelForm):
    class Meta:
        model = BankDetails
        exclude = ["seller"]
        widgets = {'account_number': forms.TextInput()}
        # 'bank_name': forms.TextInput(
        #     attrs={'placeholder': 'Bank Name'}),


class BusinessDetailsForm(ModelForm):
    class Meta:
        model = BusinessDetails
        exclude = ["seller"]
        widgets = {'pincode': forms.TextInput()}


class AddProductForm(ModelForm):
    class Meta:
        model = Products
        exclude = ["seller", ]
