from django.contrib.auth import authenticate

import os
import random
from rest_framework.exceptions import AuthenticationFailed

from api_user.models.user import User
from api_user.models.role import Role

# def register_social_user(provider, user_id, email,first_name, last_name):
#     filtered_user_by_email = User.objects.filter(email=email)
#     if filtered_user_by_email.exists():
#         print(1)
#         if provider == filtered_user_by_email[0].auth_provider:

#             registered_user = authenticate(
#                 email=email, password=os.environ.get('SOCIAL_SECRET'))

#             return {
#                 # 'username': registered_user.username,
#                 'id':registered_user.id,
#                 'email': registered_user.email,
#                 'first_name':registered_user.first_name,
#                 'last_name':registered_user.first_name,
#                 'tokens': registered_user.tokens()}

#         else:
#             raise AuthenticationFailed(
#                 detail='Please continue your login using ' + filtered_user_by_email[0].auth_provider)

#     else:
#         print(2)
#         user = {
#             'username': generate_username(first_name), 'email': email,
#             'password': os.environ.get('SOCIAL_SECRET')}
#         user = User.objects.create_user(**user)
#         user.is_verified = True
#         user.auth_provider = provider
#         user.save()

#         new_user = authenticate(
#             email=email, password=os.environ.get('SOCIAL_SECRET'))
#         return {
#             'email': new_user.email,
#             'username': new_user.username,
#             'tokens': new_user.tokens()
#         }
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
from api_oauth2.services.oauth2 import AuthorizationOauth2
import os


def register_social_user(provider,user_id, email, first_name, last_name):
    try:
        user = User.objects.get(email=email)

        if provider != user.auth_provider:
            raise AuthenticationFailed(
                detail="Please continue your login using " + user.auth_provider
            )

        # Đảm bảo người dùng được xác thực
        if user.auth_provider == "google":
            # print(user)
            # return user
            # user = authenticate(email=email, password=os.environ.get('SOCIAL_SECRET'))
            # print('user:',user.email,user.password)
            # oauth2_response =  AuthorizationOauth2.authorization_oauth2(user.email, os.environ.get('SOCIAL_SECRET'))
            # if oauth2_response.status_code == 200:
            #     # Trích xuất token từ dữ liệu phản hồi
            #     access_token = oauth2_response.json().get("access_token")
            return {
                "id": user.id,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "auth_provider": provider,
                # 'tokens': access_token
            }
        # else:
        #         # Xử lý trường hợp yêu cầu xác thực không thành công (ví dụ: token không hợp lệ)
        #     raise AuthenticationFailed('Failed to authenticate user with OAuth2')

    except User.DoesNotExist:
        # Tạo người dùng mới nếu không tồn tại
        role = Role.objects.get(name="User")
        print('',role)
        user = User.objects.create(
            email=email,
            first_name=first_name,
            last_name=last_name,
            auth_provider=provider,
        )
        user.set_password(
            os.environ.get("SOCIAL_SECRET")
        )  # Đặt mật khẩu mặc định cho tài khoản OAuth
        user.is_verified = True
        user.roles.add(role)
        user.save()

        # Xác thực người dùng mới

        # user = authenticate(email=email, password=os.environ.get("SOCIAL_SECRET"))
        # oauth2_response = AuthorizationOauth2.authorization_oauth2(
        #     user.email, user.password
        # )
        # if oauth2_response.status_code == 200:
        #     # Trích xuất token từ dữ liệu phản hồi
        #     access_token = oauth2_response.json().get("access_token")
        return {
            "email": user.email,
            # 'username': user.username,
            # "password":
        }
