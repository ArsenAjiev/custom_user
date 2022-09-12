from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from core.abs_model import CommonInfo


class Car(CommonInfo):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    engine = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[MinValueValidator(0.6), MaxValueValidator(9.9)],
    )
    year = models.IntegerField(
        validators=[MinValueValidator(1980), MaxValueValidator(2021)]
    )
    color = models.CharField(max_length=50)

    def __str__(self):
        return f'make: {self.make} - model: {self.model} - color: {self.color}'
