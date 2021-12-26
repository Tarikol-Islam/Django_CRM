from typing import Protocol
from django import forms
from django.db.models import fields

from .models import Company,Product, Order


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = []

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = []
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = []
