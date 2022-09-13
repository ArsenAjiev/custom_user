from rest_framework import mixins, viewsets
from cars.models import Car
from cars.serializers import CarSerializer


class CarViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):

    serializer_class = CarSerializer
    queryset = Car.objects.all()
