from django.db import models
from showrooms.models import ShowroomProfile
from django.core.validators import MinValueValidator
from cars.models import Car
from dealers.models import DealerProfile


class DealerSales(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    discount = models.DecimalField(
        max_digits=3, decimal_places=2, validators=[MinValueValidator(0.00)], default=0.01
    )
    start_date = models.DateField()
    end_date = models.DateField()
    dealer = models.ForeignKey(DealerProfile, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    is_active = models.BooleanField()

    def __str__(self):
        return f" Title:{self.title} -- Discount:{self.discount} --Car: {self.car.model} -- Dealer:{self.dealer.owner}"


class ShowroomSales(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    discount = models.DecimalField(
        max_digits=3, decimal_places=2, validators=[MinValueValidator(0.00)], default=0.01
    )
    start_date = models.DateField()
    end_date = models.DateField()
    showroom = models.ForeignKey(ShowroomProfile, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    is_active = models.BooleanField()

    def __str__(self):
        return f" Title:{self.title} -- Discount:{self.discount} -- Car:{self.car.model} --Showroom:{self.showroom.name}"
