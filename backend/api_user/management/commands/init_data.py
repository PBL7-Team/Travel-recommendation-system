from django.core.management.base import BaseCommand
from api_user.models import User
from api_oauth2.models import Application
from chat_history_saver.models import ChatHistory
from api_user.models.role import Role
from common.constants.gender import Genders
import random
from django.db.models import Q
from core.settings.base import (
    SECRET_KEY,
    DEFAULT_CLIENT_ID,
    DEFAULT_CLIENT_SECRET,
    SUPER_ADMIN_EMAIL,
    SUPER_ADMIN_PASSWORD,
)
from oauth2_provider.models import AbstractApplication
from django.db import transaction
from django.contrib.auth.hashers import make_password


class Command(BaseCommand):
    help = "Init data"

    def handle(self, *args, **kwargs):
        super_admin_user = self.create_superadmin_account()
        self.create_oauth2_application(user=super_admin_user)
        self.create_users()
        self.create_chathistory()

    @classmethod
    def create_oauth2_application(cls, user=None):
        # Admin page
        admin_app = Application.objects.filter(Q(client_id=DEFAULT_CLIENT_ID)).exists()
        if not admin_app:
            Application.objects.create(
                client_id=DEFAULT_CLIENT_ID,
                client_type="confidential",
                authorization_grant_type="password",
                client_secret=DEFAULT_CLIENT_SECRET,
                name="Bold Voyage Heros Admin",
                algorithm=AbstractApplication.RS256_ALGORITHM,
                scope="__all__",
                skip_authorization=True,
                type=Application.APPLICATION_TYPE_SYSTEM,
                user=user,
            )
        

    @classmethod
    def create_superadmin_account(cls):
        role, created = Role.objects.get_or_create(
            name="Super Administrator",
            description="Unlimited resources access.",
            scope="__all__",
        )
        super_admin_user = User.objects.filter(email=SUPER_ADMIN_EMAIL).first()
        # Todo: Create office if no ones exist
        if not super_admin_user:
            with transaction.atomic():
                super_admin_user = User.objects.create(
                    email=SUPER_ADMIN_EMAIL,
                    password=make_password(SUPER_ADMIN_PASSWORD, salt=SECRET_KEY),
                    first_name="Super",
                    last_name="Administrator",
                    is_superuser=True,
                    is_staff=True,
                    is_active=True,
                )
                super_admin_user.roles.add(role)
                super_admin_user.save()
        print("Initial super admin created successfully")
        return super_admin_user

    @classmethod
    def create_users(cls):
        users_data = [
            {
                "email": "ncanh2806@gmail.com",
                "first_name": "Anh",
                "last_name": "Nguyễn Công",
                "password": "password123",
                "gender": Genders.MALE,
            },
            {
                "email": "benphantom102@gmail.com",
                "first_name": "Bách",
                "last_name": "Lê Trọng",
                "password": "password123",
                "gender": Genders.FEMALE,
            },
            {
                "email": "nguyenhoang29minh03@gmail.com",
                "first_name": "Hoàng",
                "last_name": "Nguyễn Minh",
                "password": "password123",
                "gender": Genders.OTHER,
            },
            {
                "email": "namtruong0900@gmail.com",
                "first_name": "Trường",
                "last_name": "Võ Hữu Nam",
                "password": "password123",
                "gender": Genders.MALE,
            },
            {
                "email": "vinh.nd0231@gmail.com",
                "first_name": "Vinh",
                "last_name": "Trịnh Quang",
                "password": "password123",
                "gender": Genders.FEMALE,
            },
        ]

        for user_data in users_data:
            if not User.objects.filter(email=user_data["email"]).exists():
                user = User(
                    email=user_data["email"],
                    first_name=user_data["first_name"],
                    last_name=user_data["last_name"],
                    gender=user_data["gender"],
                    is_active=True,
                    is_staff=True,
                )
                user.set_password(user_data["password"])
                user.save()
                print(f"Successfully created user {user.email}")
            else:
                print(f'User with email {user_data["email"]} already exists')

        print("Initial data created successfully")

    @classmethod
    def create_chathistory(cls):
        messages_data = [
            {
                "chat_message": "Hello!",
                "system_answer": "Hi! How can I help you?",
                "descriptions": "Initial greeting",
            },
            {
                "chat_message": "What's the weather like?",
                "system_answer": "It's sunny and warm today.",
                "descriptions": "Weather inquiry",
            },
            {
                "chat_message": "Tell me a joke.",
                "system_answer": "Why don't scientists trust atoms? Because they make up everything!",
                "descriptions": "Request for a joke",
            },
            {
                "chat_message": "What time is it?",
                "system_answer": "It's 3 PM.",
                "descriptions": "Time inquiry",
            },
            {
                "chat_message": "Thank you!",
                "system_answer": "You're welcome!",
                "descriptions": "Expression of gratitude",
            },
        ]

        users = list(User.objects.all())
        if not users:
            print("No users found. Please create users first.")
            return

        for message_data in messages_data:
            user = random.choice(users)
            ChatHistory.objects.create(
                user=user,
                chat_message=message_data["chat_message"],
                system_answer=message_data["system_answer"],
                descriptions=message_data["descriptions"],
                is_from_system=False,  # You can adjust this value as needed
            )
            print(f"Successfully created chat history for user {user.email}")

        print("Initial chat history data created successfully")
