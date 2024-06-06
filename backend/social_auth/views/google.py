from rest_framework import status
from rest_framework.permissions  import AllowAny
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from social_auth.serializers import GoogleSocialAuthSerializer

class GoogleSocialAuthView(GenericAPIView):

    permission_classes=[AllowAny]
    serializer_class = GoogleSocialAuthSerializer

    def post(self, request):
        """
        POST with "auth_token"

        Send an idtoken as from google to get user information

        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = ((serializer.validated_data)['access_token'])
        return Response(data, status=status.HTTP_200_OK)



