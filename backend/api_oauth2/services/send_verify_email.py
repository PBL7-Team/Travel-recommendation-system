from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from core.settings.base import (
    EMAIL_HOST_USER
)
from api_base.services import Verification

class OAuth2Service:
    @staticmethod
    def send_verify_email(request, user):
        # print(user)
        subject = "Welcome to Our Django User Registration System"
        message = f"Hello {user.first_name}!\n\nThank you for registering on our website. Please confirm your email address to activate your account.\n\nRegards,\nThe Django Team"
        from_email = EMAIL_HOST_USER
        to_list = [user.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        # Send email confirmation link
        current_site = get_current_site(request)
        token = Verification.create_token(request.data)
        email_subject = "Confirm Your Email Address"
        message2 = render_to_string('email_confirmation.html', {
        'name': user.first_name,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': token
        })
        send_mail(email_subject, message2, from_email, to_list, fail_silently=True)
