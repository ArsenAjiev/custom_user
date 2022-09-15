from django_filters import rest_framework as filters
from cars.models import Car


class CarFilter(filters.FilterSet):
    make = filters.CharFilter()
    year = filters.RangeFilter()


    class Meta:
        model = Car
        fields = ['year', 'make']