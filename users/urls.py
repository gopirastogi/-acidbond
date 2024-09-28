from django.urls import path
from .views import send_otp, verify_otp
from . import views

urlpatterns = [
    path('send-otp/', send_otp, name='send_otp'),
    path('verify-otp/<str:email>/', verify_otp, name='verify_otp'),
]
