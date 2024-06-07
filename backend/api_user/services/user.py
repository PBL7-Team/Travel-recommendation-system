from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status

User = get_user_model()

class UserService:
    @classmethod
    def get_or_create_user(cls, profile_data):
        email = profile_data["email"]
        user, created = User.objects.get_or_create(
            email=email,
            defaults={
                'first_name': profile_data["first_name"],
                'last_name': profile_data["last_name"],
                'username': profile_data["sub"],  # hoặc bạn có thể thiết lập username khác
                'is_active': True,  # bạn có thể thiết lập các giá trị khác nếu cần
            }
        )
        return user, created