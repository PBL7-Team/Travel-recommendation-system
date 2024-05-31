from django.shortcuts import render

from rest_framework import generics, permissions, serializers

from api_user.models.user import User
from api_user.serializers import UserSerializer
# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    required_alternate_scopes = {
        "create": [["admin:users:edit"]],
        "invite": [["admin:users:edit"],],
        "retrieve": [
            ["admin:users:view"],
            ["admin:users:edit"],
        ],
        "update": [
            ["users:edit-mine"],
            ["admin:users:edit"],
        ],
        "destroy": [["admin:users:edit"]],
        "multiple_delele": [["admin:users:edit"]],
        "list": [["admin:users:view"], ["admin:users:edit"]],
        "change_password": [["users:edit-mine"]],
        "import_data": [["admin:users:edit"]],
    }
    
    def get_permissions(self):
        """Every one can see the list and detail of plans"""

        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return super().get_permissions()
