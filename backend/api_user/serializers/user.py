from rest_framework import generics, permissions, serializers

from api_user.models.user import User
from api_user.models.role import Role
from django.contrib.auth.hashers import make_password


# first we define the serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name"]


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "password", "first_name", "last_name"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        role = Role.objects.get(name="User")
        user.roles.add(role)
        user.set_password(validated_data["password"])
        user.is_active = True
        user.is_staff = True
        user.is_superuser = False
        user.save()
        return user
