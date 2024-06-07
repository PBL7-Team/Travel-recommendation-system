import threading

from django.conf import settings
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

class MailingThread(threading.Thread):
    def __init__(
        self,
        messages=None,
        fail_callback=None
    ):
        self.messages = messages
        self.fail_callback =  fail_callback
        threading.Thread.__init__(self)

    def run(self):
        for message in self.messages:
            try:
                message.send()
            except Exception as e:
                # TODO: Add a log right here
                print(str(e))
                if self.fail_callback:
                    self.fail_callback(message)


class Mailing:
    @staticmethod
    def async_send_messages(messages):
        MailingThread(messages=messages).start()

    @classmethod
    def create_html_message(cls, data, attachment=None, headers=None):
        subject = data.get("subject")
        from_email=data.get("from") or settings.DEFAULT_FROM_EMAIL 
        to = data.get("to")

        html_content = render_to_string(
            data.get("template"), data.get("context")
        )
        text_content = strip_tags(html_content)

        msg = EmailMultiAlternatives(
            subject, text_content, from_email, to, headers
        )
        msg.attach_alternative(html_content, "text/html")
        if attachment:
            msg.attach(
                attachment.filename,
                attachment.content,
                attachment.mimetype,
            )
        return msg


from datetime import datetime

import jwt
from django.conf import settings
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext as _

from .base import BaseService


class Verification(BaseService):
    @staticmethod
    def get_header():
        return {"alg": "HS256", "typ": "JWT"}

    @staticmethod
    def get_secret_key():
        return settings.SECRET_KEY

    @staticmethod
    def create_token(data, life_time=3600):
        print('data',data)
        if not isinstance(data, dict):
            raise ValidationError(detail=_("Invalid format"))
        
        payload = data.copy()
        payload.update()
        {
            "iat": datetime.now().timestamp(),
            "exp": datetime.now().timestamp() + life_time
        }

        token = jwt.encode(payload, Verification.get_secret_key(), algorithm="HS256")
        return token

    @staticmethod
    def decode_token(token):
        payload = jwt.decode(token, Verification.get_secret_key(), algorithms=["HS256"])
        if 'iat' in payload:
            del payload['iat']
        
        if 'exp' in payload:
            exp = int(payload.get("exp"))
            if datetime.now().timestamp() < exp:
                return None
            del payload['exp']
        return payload
