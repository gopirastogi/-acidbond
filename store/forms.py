# forms.py
from django import forms
from .models import Customer, Order


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address_line_1', 'address_line_1', 'city', 'state', 'postal_code']
        # Adjust fields based on your Customer model
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control', 
                'id': 'account-fn', 
                'required': False,
                'value': ''
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control', 
                'id': 'account-ln', 
                'required': False,
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 
                'id': 'account-email', 
                'required': False, 
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control', 
                'id': 'account-phone', 
                'required': False,
            }),
            'address_line_1': forms.TextInput(attrs={
                'class': 'form-control', 
                'id': 'account-address-line-1', 
                'required': False
            }),
            'address_line_2': forms.TextInput(attrs={
                'class': 'form-control', 
                'id': 'account-address-line-2'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control', 
                'id': 'account-city', 
                'required': False
            }),
            'state': forms.TextInput(attrs={
                'class': 'form-control', 
                'id': 'account-state', 
                'required': False
            }),
            'postal_code': forms.TextInput(attrs={
                'class': 'form-control', 
                'id': 'account-postal-code', 
                'required': True
            }),
        }