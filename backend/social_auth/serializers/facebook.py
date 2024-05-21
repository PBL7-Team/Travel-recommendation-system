from rest_framework import serializers
import os
from rest_framework.exceptions import AuthenticationFailed
from social_auth.utils import Facebook,register_social_user


class FacebookSocialAuthSerializer(serializers.Serializer):
    """Handles serialization of facebook related data"""
    access_token = serializers.CharField()

    def validate_access_token(self, access_token):
        user_data = Facebook.validate(access_token)

        try:
            user_id = user_data['id']
            email = user_data['email']
            name = user_data['name']
            provider = 'facebook'
            return register_social_user(
                provider=provider,
                user_id=user_id,
                email=email,
                name=name
            )
        except Exception as identifier:

            raise serializers.ValidationError(
                'The token  is invalid or expired. Please login again.'
            )
