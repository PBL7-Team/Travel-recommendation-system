import api_oauth2
from google.auth.transport.requests import Request
from .oauth2 import AuthorizationOauth2
from api_user.services.user import UserService
from core.settings.base import EMAIL_DOMAIN, LIMIT_DOMAIN, GOOGLE_CLIENT_ID
from google.oauth2 import id_token
from rest_framework import status
from rest_framework.response import Response

GOOGLE_ID_TOKEN_INFO_URL = "https://www.googleapis.com/oauth2/v3/tokeninfo"


class GoogleService:
    @classmethod
    def google_get_user_profile(cls, token: str):
        try:
            request = Request()
            id_info = id_token.verify_oauth2_token(token, request, GOOGLE_CLIENT_ID)
            if "accounts.google.com" in id_info["iss"]:
                return id_info
        except Exception as e:
            print(e)
            return False

    @classmethod
    def login_google(cls, credential):
        user_data = cls.google_get_user_profile(credential)
        if not user_data:
            return Response(
                {"Token": "The token is either invalid or has expired"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        profile_data = {
            "sub": user_data["sub"],
            "email": user_data["email"],
            "first_name": user_data["given_name"],
            "last_name": user_data["family_name"],
            "iss": user_data["iss"],
        }
        if LIMIT_DOMAIN is False or (
            LIMIT_DOMAIN is True and user_data["email"].split("@")[1] == EMAIL_DOMAIN
        ):
            user, _ = UserService.get_or_create_user(profile_data)
            if user is None:
                return Response(
                    {"Unauthorized": "Our account has not been linked"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
            password = credential
            request_oauth2 = AuthorizationOauth2.authorization_oauth2(
                user.email, password
            )
            data = request_oauth2.json()
            if request_oauth2.status_code == 200:
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

        return Response(
            {"error": "You cannot login with this email"},
            status=status.HTTP_400_BAD_REQUEST,
        )
