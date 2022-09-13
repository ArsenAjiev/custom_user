from django.db import models
from django.contrib.auth.models import AbstractUser


# base class for all models
class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_dealer = models.BooleanField(default=False)
    is_showroom = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['is_customer', 'is_dealer', 'is_showroom', 'email']

    def __str__(self):
        return self.username



