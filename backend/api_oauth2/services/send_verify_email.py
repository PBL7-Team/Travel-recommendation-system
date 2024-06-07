from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from api_base.services.mailing import Mailing
from django.utils.translation import gettext as _
from core.settings.base import (
    EMAIL_HOST_USER
)
from django.conf import settings
from api_base.services import Verification

class OAuth2Service:
    @staticmethod
    def send_verify_email(request, user):
        # print(user)
        # subject = "Welcome to Our Django User Registration System"
        # message = f"Hello {user.first_name}!\n\nThank you for registering on our website. Please confirm your email address to activate your account.\n\nRegards,\nThe Django Team"
        # from_email = EMAIL_HOST_USER
        data= {
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name
        }
        host = settings.API_HOST
        admin_scheme = (
            "http"
            if host.startswith("localhost") or host.startswith("127.0.0.1")
            else "https"
        )
        token = Verification.create_token(data=data)
        link = f"{admin_scheme}://{host}/businesses/verify?token={token}"
        # to_list = [user.email]
        # send_mail(subject, message, from_email, to_list, fail_silently=True)
        # Send email confirmation link
        # current_site = get_current_site(request)
        data = {
            "template": "verify_personal_email.html",
            "subject": _("Welcome to Our Bold Voyage Heroes Traveler Recommend System"),
            "context": {
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "token": token,
                "link": link,
                # "logo": logo,
                "lang": "en"
            },
            "to": [user.email],
        }
        message = Mailing.create_html_message(data=data)
        Mailing.async_send_message(message=message)
