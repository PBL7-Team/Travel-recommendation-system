from django.shortcuts import render

# Create your views here.
import json
from django.http import HttpResponse
from oauth2_provider.signals import app_authorized
from oauth2_provider.models import get_access_token_model
from oauthlib.oauth2.rfc6749.utils import list_to_scope
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.debug import sensitive_post_parameters
from oauth2_provider.views.mixins import OAuthLibMixin
from rest_framework.response import Response
from django.utils.translation import gettext as _
from api_user.serializers import CreateUserSerializer
from api_user.services.user import UserService
from api_oauth2.services import OAuth2Service
from core.settings.base import (
    DEFAULT_CLIENT_ID,
    DEFAULT_CLIENT_SECRET,
    COMMON_CLIENT_ID,
    COMMON_CLIENT_SECRET,
)
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_404_NOT_FOUND,
    HTTP_403_FORBIDDEN,
    HTTP_406_NOT_ACCEPTABLE,
    HTTP_500_INTERNAL_SERVER_ERROR,
)

from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from django.contrib.auth import authenticate

# from ..services import GoogleService
# from core.settings.base import EMAIL_DOMAIN, LIMIT_DOMAIN
# from api_user.services import UserService

from rest_framework.permissions import AllowAny, IsAuthenticated
from django.http import HttpRequest
from django.contrib.auth import get_user_model
import requests
from oauth2_provider.contrib.rest_framework import TokenMatchesOASRequirements

from ..services import GoogleService
from core.settings.base import EMAIL_DOMAIN, LIMIT_DOMAIN, GOOGLE_CLIENT_ID

User = get_user_model()
AccessToken = get_access_token_model()
# class Oauth2ViewSet(OAuthLibMixin, ViewSet):
#     """
#     The endpoint for login, login with GG, refresh token and logout
#     """

#     def get_permissions(self):
#         """Returns the permission based on the type of action"""

#         if self.action in ["login", "loginWithGoogle"]:
#             return [AllowAny()]

#         return [IsAuthenticated()]

#     @action(detail=False, methods=["post"], url_path="login")
#     def login(self, request, pk=None):
#         request.POST._mutable = True
#         request.POST.update(
#             {
#                 "grant_type": "password",
#                 "client_id": DEFAULT_CLIENT_ID,
#                 "client_secret": DEFAULT_CLIENT_SECRET,
#             }
#         )
#         url, headers, body, status = self.create_token_response(request)
#         if status == 200:
#             access_token = json.loads(body).get("access_token")
#             if access_token is not None:
#                 token = get_access_token_model().objects.get(token=access_token)
#                 app_authorized.send(sender=self, request=request, token=token)
#         response = HttpResponse(content=body, status=status)

#         for k, v in headers.items():
#             response[k] = v
#         return response

#     @action(detail=False, methods=["post"], url_path="refresh-token")
#     def refeshToken(self, request):
#         request.POST._mutable = True
#         refresh_token =  request.POST.get("refresh_token")
#         request.POST.update(
#             {
#                 "grant_type": "refresh_token",
#                 "client_id": DEFAULT_CLIENT_ID,
#                 "client_secret": DEFAULT_CLIENT_SECRET,
#                 "refresh_token": refresh_token,
#             }
#         )
#         url, headers, body, status = self.create_token_response(request)
#         if status == 200:
#             access_token = json.loads(body).get("access_token")
#             if access_token is not None:
#                 token = get_access_token_model().objects.get(token=access_token)
#                 app_authorized.send(sender=self, request=request, token=token)
#         response = HttpResponse(content=body, status=status)

#         for k, v in headers.items():
#             response[k] = v
#         return Response(response, status=status.HTTP_200_OK)

#     @action(detail=False, methods=["post"], url_path="logout")
#     def logout(self, request, pk=None):
#         request.POST._mutable = True
#         refresh_token = request.POST.get("refresh_token")
#         access_token = request.POST.get("access_token")

#         # revoke refresh_token first, to make user can not renew access_token
#         request.POST.update(
#             {
#                 "client_id": DEFAULT_CLIENT_ID,
#                 "client_secret": DEFAULT_CLIENT_SECRET,
#                 "token_type_hint": "refresh_token",
#                 "token": refresh_token,
#             }
#         )
#         url, headers, body, status = self.create_revocation_response(request)
#         if status != HTTP_200_OK:
#             return HttpResponse(
#                 content={"error": "can not revoke refresh_token"},
#                 status=HTTP_400_BAD_REQUEST,
#             )

#         # revoke access_token
#         request.POST.update(
#             {
#                 "token_type_hint": "access_token",
#                 "token": access_token,
#             }
#         )
#         url, headers, body, status = self.create_revocation_response(request)
#         if status != HTTP_200_OK:
#             return HttpResponse(
#                 content={"error": "can not revoke access_token"},
#                 status=HTTP_400_BAD_REQUEST,
#             )

#         return Response({"message": "logout success!"}, status=HTTP_200_OK)


class Oauth2ViewSet(OAuthLibMixin, ViewSet):
    """
    The endpoints for login, refresh token and logout
    """

    required_alternate_scopes = ["read", "write"]  # Define your required scopes here

    def get_permissions(self):
        """Returns the permission based on the type of action"""
        if self.action in ["login", "register", "refresh_token","loginWithGoogle"]:
            return [AllowAny()]
        return [IsAuthenticated()]

    @action(
        detail=False,
        methods=["post"],
        url_path="register",
        permission_classes=[AllowAny],
        authentication_classes=[],
    )
    def register(self, request):
        """
        Registers user to the server. Input should be in the format:
        {"username": "username", "password": "1234abcd"}
        """
        # Put the data from the request into the serializer
        serializer = CreateUserSerializer(data=request.data)
        # Validate the data
        if serializer.is_valid():
            # If it is valid, save the data (creates a user).
            user = serializer.save()
            # Then we get a token for the created user.
            # This could be done differentley

            # r = requests.post('http://127.0.0.1:8000/o/token/',
            #     data={
            #         'grant_type': 'password',
            #         'username': request.data['email'],
            #         'password': request.data['password'],
            #         'client_id': DEFAULT_CLIENT_ID,
            #         'client_secret': DEFAULT_CLIENT_ID,
            #     },
            # )
            # request.POST._mutable = True
            # request.POST.update(
            #     {
            #         "grant_type": "password",
            #         "client_type": "confidential",
            #         'username': request.data['email'],
            #         'password': request.data['password'],
            #         "client_id": DEFAULT_CLIENT_ID,
            #         "client_secret": DEFAULT_CLIENT_SECRET,
            #        # "scope": list_to_scope(scopes)
            #     }
            # )
            # url, headers, body, status = self.create_token_response(request)
            # if status == 200:
            #     access_token = json.loads(body).get("access_token")
            #     if access_token is not None:
            #         token = AccessToken.objects.get(token=access_token)
            #         app_authorized.send(sender=self, request=request, token=token)
            # response = HttpResponse(content=body, status=status)

            # for k, v in headers.items():
            #     response[k] = v
            # return response

            # Send welcome email
            try:
                OAuth2Service.send_verify_email(request, user)
                return Response(
                    {"message": _("The invitation have been sent.")}, status=HTTP_200_OK
                )
            except Exception as e:
                print(e)
                return Response(
                    {"message": _("There is an error occur.")},
                    status=HTTP_500_INTERNAL_SERVER_ERROR,
                )

        return Response(serializer.errors, status=HTTP_401_UNAUTHORIZED)

    @action(
        detail=False,
        methods=["post"],
        url_path="login",
        permission_classes=[AllowAny],
        authentication_classes=[],
    )
    def login(self, request, pk=None):
        try:
            user_name = request.POST.get("username")
            password = request.POST.get("password")
            if not user_name or not password:
                return Response(
                    {"error": _("Username and password are required.")},
                    status=HTTP_404_NOT_FOUND,
                )
            user = authenticate(username=user_name, password=password)
            if user is None:
                return Response(
                    {"error": _("Invalid username or password.")},
                    status=HTTP_404_NOT_FOUND,
                )

            # user = User.objects.prefetch_related("roles").get(email=user_name)
            # # This is not administrator account
            # if user.roles is None:
            #     raise User.DoesNotExist(message = 'The user is not Admin')
        except User.DoesNotExist:
            return Response(
                {"error": _("The user does not exist.")},
                status=HTTP_404_NOT_FOUND,
            )
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
                "scope": list_to_scope(scopes),
            }
        )
        url, headers, body, status = self.create_token_response(request)
        if status == 200:
            access_token = json.loads(body).get("access_token")
            if access_token is not None:
                token = AccessToken.objects.get(token=access_token)
                app_authorized.send(sender=self, request=request, token=token)
        response = HttpResponse(content=body, status=status)
        print("r", response)

        for k, v in headers.items():
            response[k] = v
        return response

    @action(
        detail=False,
        methods=["post"],
        url_path="refresh-token",
        permission_classes=[AllowAny],
        authentication_classes=[],
    )
    def refreshToken(self, request):
        request.POST._mutable = True
        refresh_token = request.POST.get("refresh_token")
        if not refresh_token or refresh_token == "null":
            return Response(
                {"error": _("Invalid token")},
                status=HTTP_406_NOT_ACCEPTABLE,
            )
        request.POST.update(
            {
                "grant_type": "refresh_token",
                "client_id": DEFAULT_CLIENT_ID,
                "client_secret": DEFAULT_CLIENT_SECRET,
                "refresh_token": refresh_token,
            }
        )
        url, headers, body, status = self.create_token_response(request)
        if status == 200:
            access_token = json.loads(body).get("access_token")
            if access_token is not None:
                token = AccessToken.objects.get(token=access_token)
                app_authorized.send(sender=self, request=request, token=token)
        response = HttpResponse(content=body, status=status)

        for k, v in headers.items():
            response[k] = v
        return response

    @action(detail=False, methods=["post"], url_path="logout")
    def logout(self, request, pk=None):
        request.POST._mutable = True
        refresh_token = request.POST.get("refresh_token")
        access_token = request.POST.get("access_token")

        # revoke refresh_token first, to make user can not renew access_token
        request.POST.update(
            {
                "client_id": DEFAULT_CLIENT_ID,
                "client_secret": DEFAULT_CLIENT_SECRET,
                "token_type_hint": "refresh_token",
                "token": refresh_token,
            }
        )
        url, headers, body, status = self.create_revocation_response(request)
        if status != HTTP_200_OK:
            return HttpResponse(
                content={"error": "can not revoke refresh_token"},
                status=HTTP_400_BAD_REQUEST,
            )

        # revoke access_token
        request.POST.update(
            {
                "token_type_hint": "access_token",
                "token": access_token,
            }
        )
        url, headers, body, status = self.create_revocation_response(request)
        if status != HTTP_200_OK:
            return HttpResponse(
                content={"error": "can not revoke access_token"},
                status=HTTP_400_BAD_REQUEST,
            )

        return Response({"message": "logout success!"}, status=HTTP_200_OK)

    @action(
        detail=False,
        methods=["post"],
        url_path="login/google",
        permission_classes=[AllowAny],
    )
    def loginWithGoogle(self, request):
        request.POST._mutable = True
        credential = request.POST.get("credential")
        print(credential)
        user_data = GoogleService.google_get_user_profile(credential)
        if not user_data:
            return Response(
                {"Token": "The token is either invalid or has expired"},
                status=HTTP_401_UNAUTHORIZED,
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
            user, created = UserService.get_or_create_user(profile_data)
            if created:
                # Xử lý khi người dùng được tạo mới (nếu cần)
                print("hi")
                pass

            password = credential

            request.POST.update(
                {
                    "grant_type": "public",
                    "grant_type": "password",
                    "client_id": DEFAULT_CLIENT_ID,
                    "client_secret": DEFAULT_CLIENT_SECRET,
                    "username": user.email,
                    "password": password,
                }
            )
            url, headers, body, status = self.create_token_response(request)
            if status == 200:
                access_token = json.loads(body).get("access_token")
                if access_token is not None:
                    token = get_access_token_model().objects.get(token=access_token)
                    app_authorized.send(sender=self, request=request, token=token)
            response = HttpResponse(content=body, status=status)

            for k, v in headers.items():
                response[k] = v
            return response

        return Response(
            {"Unauthorized": "The domain were blocked."},
            status=HTTP_401_UNAUTHORIZED,
        )
