from django.db import models
from users.models import User
from core.abs_model import CommonInfo
from cars.models import Car

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.is_customer:
        CustomerProfile.objects.create(owner=instance)


# CustomerProfile created automatically when creating a Customer
class CustomerProfile(CommonInfo):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)
    customer_query = models.JSONField(
        default=dict(
            {
                "make": "",
                "model": "",
                "engine": "",
                "year": "",
                "color": "",
                "price": "",
            }
        )
    )
    balance = models.DecimalField(
        max_digits=15, decimal_places=2, validators=[MinValueValidator(0.00)], default=0
    )

    cars = models.ManyToManyField(Car, through="CustomerCar")

    def __str__(self):
        return f"title: {self.title} - balance: {self.balance}"


# cars bought by the user
class CustomerCar(CommonInfo):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
    showroom = models.ForeignKey("dealers.DealerProfile", on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
    price = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        validators=[MinValueValidator(0.00)],
        default=0.00,
    )

    def __str__(self):
        return f"Car_make:{self.car.make} -- Customer_owner:{self.customer.owner}"
