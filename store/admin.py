from django.contrib import admin
from .models import Customer, Order, OrderItem

admin.site.register(OrderItem)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'city', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number', 'city')
    list_filter = ('city', 'state', 'country')
    ordering = ('-created_at', 'updated_at')

admin.site.register(Customer, CustomerAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'status', 'total_price', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at', 'updated_at', 'country')
    search_fields = ('id', 'customer__first_name', 'customer__last_name', 'email', 'phone_number')
    ordering = ('-created_at',)
    readonly_fields = ('id', 'created_at', 'updated_at')

    fieldsets = (
        ('Order Information', {
            'fields': ('id', 'customer', 'user', 'status', 'total_price')
        }),
        ('Shipping Information', {
            'fields': ('first_name', 'last_name', 'email', 'phone_number', 'country', 'add1', 'add2', 'postal_code')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )

admin.site.register(Order, OrderAdmin)