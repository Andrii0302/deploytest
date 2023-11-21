from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)  # Change to EmailField for proper email validation
    password = models.CharField(max_length=255)
    username = None

    email_verified = models.BooleanField(default=False)  # Add this line for email verification

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class PasswordReset(models.Model):
    email = models.EmailField(max_length=255)  # Change to EmailField for consistency
    token = models.CharField(max_length=255, unique=True)
