from django.db import models
from users.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.is_customer:
        DealerProfile.objects.create(owner=instance)


# CustomerProfile created automatically when creating a Customer
class DealerProfile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.title}"
