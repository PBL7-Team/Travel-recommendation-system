from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
       
    def create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_staff = False
        user.is_superuser = False
        user.is_active = True
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password, **extra_fields):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user
