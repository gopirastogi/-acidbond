# forms.py
from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['address', 'city', 'country', 'postal_code', 'email', 'phone_number']
