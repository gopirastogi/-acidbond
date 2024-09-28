from django.urls import path, include
from cartt import views
from uuid import UUID
from .views import order_detail 
urlpatterns = [
 
    path('', views.cart, name='cart'),
    path('mans/', views.mans, name='mans'),
    path('test/', views.test, name='test'),
    path('cart/remove/<uuid:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('add_to_cart/<uuid:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart_view/', views.cart_view, name='cart_view'),
    path('order/<uuid:order_id>/', order_detail, name='order_detail'),
    
    
]