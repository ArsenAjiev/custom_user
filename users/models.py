from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db.models.signals import post_save
from django.dispatch import receiver


# base class for all models
class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_dealer = models.BooleanField(default=False)
    is_showroom = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['is_customer', 'is_dealer', 'is_showroom', 'email']

    def __str__(self):
        return self.username


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created and instance.is_customer:
#         CustomerProfile.objects.create(owner=instance)
#
#
# # CustomerProfile created automatically when creating a Customer
# class CustomerProfile(models.Model):
#     owner = models.OneToOneField(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=255, blank=True, null=True)
#
#     def __str__(self):
#         return f"{self.title}"
