from django.db import models
from users.models import User
from core.abs_model import CommonInfo
from cars.models import Car


from django_countries.fields import CountryField

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.is_showroom:
        ShowroomProfile.objects.create(owner=instance)


# ShowroomProfile created automatically when creating a Customer
class ShowroomProfile(CommonInfo):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    location = CountryField(blank=True, null=True)
    showroom_query = models.JSONField(
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
    car = models.ManyToManyField(Car, through="ShowroomCar")

    def __str__(self):
        return f"Owner:{self.owner.username} -- Name:{self.name} - Balance:{self.balance}"


class ShowroomCar(CommonInfo):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    showroom = models.ForeignKey(ShowroomProfile, on_delete=models.CASCADE)
    dealer = models.ForeignKey("dealers.DealerProfile", on_delete=models.CASCADE)
    price = models.DecimalField(
        max_digits=15, decimal_places=2, validators=[MinValueValidator(0.00)], default=0
    )
    count = models.IntegerField(default=1)

    class Meta:
        # there cannot be the same combinations
        unique_together = ('car', 'dealer', 'showroom')

    def __str__(self):
        return f"Car:{self.car.make} -- Model:{self.car.model} -- Count:{self.count}\
         Price:{self.price} -- Showroom:{self.showroom.owner.username}"


class TransactionToCustomer(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey("customers.CustomerProfile", on_delete=models.CASCADE)
    showroom = models.ForeignKey(ShowroomProfile, on_delete=models.CASCADE)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)], default=0
    )
    count = models.IntegerField(default=1)

    def __str__(self):
        return f" Car:{self.car.make}-- Model:{self.car.model} -- Price: {self.price} -- Count: {self.count} \
         -- Customer: {self.customer.owner} -- Showroom:~{self.showroom.owner}"
