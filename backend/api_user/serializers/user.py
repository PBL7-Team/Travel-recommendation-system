from rest_framework import generics, permissions, serializers

from api_user.models.user import User
from api_user.models.role import Role


# first we define the serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name"]


class CreateUserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        role = Role.objects.get(
            name="User",
        )
        user.roles.add(role)
        user.is_active= False
        user.save()
        return user

    class Meta:
        model = User
        fields = ["id", "email", "password", "first_name", "last_name"]
        extra_kwargs = {"password": {"write_only": True}}
