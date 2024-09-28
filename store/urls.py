from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
 
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('base/', views.base, name='base'),
    path('mail/', views.mail, name='mail'),
    path('profile/orders/', views.orders, name='orders'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout_success/', views.checkout_success, name='checkout_success'),
    path('profile/', views.profile_view, name='profile_view'),  # Ensure UUID pattern is correct
    path('place/', views.place, name='place'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/create/', views.create_customer, name='create_customer'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('invoice/', views.generate_invoice, name='generate_invoice'), 

]