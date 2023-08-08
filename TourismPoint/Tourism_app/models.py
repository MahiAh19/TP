from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

# Create your models here.

class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user. """
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return a new super user"""
        user = self.create_user(email, password)
        user.is_superuser = True
        user.save(using=self._db)

        return user


class Customer(models.Model):
    name = models.CharField(max_length= 100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Queries(models.Model):
    destination = models.CharField(max_length= 20)
    departure = models.CharField(max_length= 20)
    date_of_travel = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.customer.name} - {self.destination}"