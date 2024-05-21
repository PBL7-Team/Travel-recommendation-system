from rest_framework import serializers
from social_auth.utils import Google,register_social_user
import os
from rest_framework.exceptions import AuthenticationFailed
from social_auth.utils.google import Google

class GoogleSocialAuthSerializer(serializers.Serializer):
    access_token = serializers.CharField()  

    def validate_access_token(self, access_token):
        user_data = Google.validate(access_token)
        try:
            user_data['sub']
        except:
            raise serializers.ValidationError(
                'The token is invalid or expired. Please login again.'
            )

        if user_data['aud'] != os.environ.get('DJANGO_GOOGLE_OAUTH2_CLIENT_ID'):

            raise AuthenticationFailed('oops, who are you?')

        user_id = user_data['sub']
        email = user_data['email']
        # name = user_data['name']
        first_name= user_data['given_name']
        last_name= user_data['family_name']
        provider = 'google'

        return register_social_user(
            provider=provider, user_id=user_id, email=email, first_name=first_name, last_name=last_name)

