from django.shortcuts import render, redirect, HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import EmailOTP
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import login, get_user_model
from store.models import Customer


# Create your views here.

User = get_user_model()

def send_otp(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        otp_entry, created = EmailOTP.objects.get_or_create(email=email)
        otp_entry.generate_otp()

        # Send OTP via email
        send_mail(
            'Your OTP Code',
            f'Your OTP code is {otp_entry.otp}',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

        return redirect('verify_otp', email=email)

    return render(request, 'send_otp.html')



def verify_otp(request, email):
    if request.method == 'POST':
        otp_code = request.POST.get('otp_code')
        otp_entry = get_object_or_404(EmailOTP, email=email)

        if otp_entry.otp == otp_code:
            # Check if the user exists
            user = User.objects.filter(email=email).first()
            if user is None:
                # Create a new user if not exists
                user = User.objects.create_user(username=email, email=email)

            # Specify the backend explicitly
            backend = 'django.contrib.auth.backends.ModelBackend'  # Adjust if you're using a different backend
            user.backend = backend

            # Log the user in
            login(request, user, backend=backend)
            return redirect('/profile/create/')
        else:
            return render(request, 'verify_otp.html', {'error': 'Invalid OTP', 'email': email})

    return render(request, 'verify_otp.html', {'email': email})