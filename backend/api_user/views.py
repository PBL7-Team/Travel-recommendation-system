from django.shortcuts import render

from rest_framework import generics, permissions, serializers
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from api_user.models.user import User
from api_user.serializers import UserSerializer
# Create your views here.
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer