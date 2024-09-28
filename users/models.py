from django.db import models
import random
import secrets
import datetime
from django.utils import timezone

class EmailOTP(models.Model):
    email = models.EmailField(unique=True)
    otp = models.CharField(max_length=6, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def generate_otp(self):
        """Generates a random 6-digit OTP"""
        self.otp = random.randint(100000, 999999)
        self.save()

    def __str__(self):
        return f'{self.email} - {self.otp}'
