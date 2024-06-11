from rest_framework import status
import os
import json
from django.http import HttpResponse
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
import rest_framework.status
from social_auth.serializers import GoogleSocialAuthSerializer
from rest_framework.views import APIView
from core.settings.base import (
    DEFAULT_CLIENT_ID,
    DEFAULT_CLIENT_SECRET,
)

from social_auth.utils import register_social_user
from django.contrib.auth import get_user_model
from oauth2_provider.models import get_access_token_model
from oauth2_provider.signals import app_authorized
from oauth2_provider.views.mixins import OAuthLibMixin
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from oauthlib.oauth2.rfc6749.utils import list_to_scope

User = get_user_model()
AccessToken = get_access_token_model()
# class GoogleSocialAuthView(GenericAPIView):

#     permission_classes = [AllowAny]
#     serializer_class = GoogleSocialAuthSerializer

#     def post(self, request):
#         """
#         POST with "auth_token"

#         Send an idtoken as from google to get user information

#         """
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         data = (serializer.validated_data)["access_token"]
#         return Response(data, status=status.HTTP_200_OK)


class GoogleSocialAuthView(OAuthLibMixin, ViewSet):

    required_alternate_scopes = ["read", "write"]
    permission_classes = [AllowAny]
    serializer_class = GoogleSocialAuthSerializer

    @action(
        detail=False,
        methods=["post"],
        url_path="login",
        permission_classes=[AllowAny],
        authentication_classes=[],
    )
    def loginByGoogle(self, request):
        """
        POST with "auth_token"
        Send an idtoken as from Google to get user information and return an access token.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Lấy thông tin người dùng từ token Google
        user_data = serializer.validated_data["user_data"]
        email = user_data.get("email")

        if not email:
            return Response({"error": "Invalid user data"}, status=status.HTTP_400_BAD_REQUEST)

        # Lấy thông tin người dùng hoặc tạo người dùng mới
        user_info = register_social_user(
            provider=user_data["provider"],
            user_id=user_data["user_id"],
            email=user_data["email"],
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
        )
        print("user:", user_info)
        email = user_info.get('email')
        user = User.objects.get(email=email)
        scopes = set()
        for role in user.roles.all():
            scopes = scopes.union(set(role.scopes.keys()))
        request.POST._mutable = True
        request.POST.update(
            {
                "grant_type": "password",
                "client_type": "confidential",
                "client_id": DEFAULT_CLIENT_ID,
                "client_secret": DEFAULT_CLIENT_SECRET,
                "username": email,
                "password": os.environ.get("SOCIAL_SECRET"),
                "scope": list_to_scope(scopes),
            }
        )
        print('okay')
        # Tạo token OAuth2
        url, headers, body, status = self.create_token_response(request)
        print('body',body)
        if status == 200:
            access_token = json.loads(body).get("access_token")
            if access_token:
                token = AccessToken.objects.get(token=access_token)
                app_authorized.send(sender=self, request=request, token=token)

        response = HttpResponse(content=body, status=status)
        for k, v in headers.items():
            response[k] = v
        return response
