from django.contrib import admin
from .models import Category, Product, ContactUs, CartItem

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ContactUs)
admin.site.register(CartItem)

