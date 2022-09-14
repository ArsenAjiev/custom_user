from django.db import models
from users.models import User
from cars.models import Car
from core.abs_model import CommonInfo
from django.core.validators import MinValueValidator, MaxValueValidator

from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.is_dealer:
        DealerProfile.objects.create(owner=instance)


# DealerProfile created automatically when creating a Customer
class DealerProfile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.IntegerField(
        default=1990, validators=[MinValueValidator(1990), MaxValueValidator(2022)]
    )
    description = models.TextField(blank=True, null=True)
    car = models.ManyToManyField(Car, through="DealerCar")
    balance = models.DecimalField(
        max_digits=15, decimal_places=2, validators=[MinValueValidator(0.00)], default=0
    )

    def __str__(self):
        return f"{self.owner.username} - {self.title} - {self.balance}"


class DealerCar(CommonInfo):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    dealer = models.ForeignKey(DealerProfile, on_delete=models.CASCADE)
    price = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        validators=[MinValueValidator(0.00)],
        default=0.00,
    )
    count = models.IntegerField(default=1)

    class Meta:
        # there cannot be the same combinations
        unique_together = ('car', 'dealer',)

    def __str__(self):
        return f"Car_make:{self.car.make} -- Model: {self.car.model} -- Price:{self.price} -- Count:{self.count} -- Dealer: {self.dealer.owner}"


class TransactionToShowroom(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    showroom = models.ForeignKey("showrooms.ShowroomProfile", on_delete=models.CASCADE)
    dealer = models.ForeignKey(DealerProfile, on_delete=models.CASCADE)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)], default=0
    )
    count = models.IntegerField(default=1)

    def __str__(self):
        return f" Car_make:{self.car.make} Model: {self.car.model} -- Price: {self.price} -- Count: {self.count} \
         -- Showroom:{self.showroom.owner} -- Dealer: {self.dealer.owner}"
