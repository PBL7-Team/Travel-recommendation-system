from django.db import models

# Create your models here.
import uuid

from api_base.manager import UserManager
from backend.api_user.models.user import Title
from api_user.models.role import Role
from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from backend.common.constants.gender import Genders


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    password = models.CharField(verbose_name="password", max_length=255)
    email = models.EmailField(max_length=255, unique=True, null=True)
    name = models.CharField(max_length=255, null=True)
    active = models.BooleanField(default=True)
    roles = models.ManyToManyField(Role, related_name="users", null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(
        choices=Genders.GENDERS, default=Genders.Select, max_length=100
    )
    USERNAME_FIELD = "email"  # username

    objects = UserManager()

    class Meta:
        db_table = "users"

    def __str__(self):
        return str(self.id)

    @property
    def is_active(self):
        return self.active

    def set_password(self, raw_password):
        self.password = make_password(password=raw_password, salt=settings.SECRET_KEY)
        self._password = raw_password

    def get_title(self):
        return " ,".join([title.title for title in self.title.all()])