from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import authenticate, login, logout
from api_base.services.mailing import Mailing, Verification
from core.settings.base import (
    EMAIL_HOST_USER
)

from api_base.services import Mailing, Verification

def send_verify_email(request,user):
    subject = "Welcome to Our Django User Registration System"
    message = f"Hello {user.first_name}!\n\nThank you for registering on our website. Please confirm your email address to activate your account.\n\nRegards,\nThe Django Team"
    from_email = EMAIL_HOST_USER
    to_list = [user.email]
    send_mail(subject, message, from_email, to_list, fail_silently=True)
    # Send email confirmation link
    current_site = get_current_site(request)
    email_subject = "Confirm Your Email Address"
    message2 = render_to_string('email_confirmation.html', {
    'name': user.first_name,
    'domain': current_site.domain,
    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
    'token': Verification.create_token(user)
    })
    
