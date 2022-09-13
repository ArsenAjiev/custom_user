from rest_framework import mixins, viewsets
from cars.models import Car
from cars.serializers import CarSerializer


class CarViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):

    serializer_class = CarSerializer
    queryset = Car.objects.all()
