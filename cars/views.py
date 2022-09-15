from rest_framework import mixins, viewsets
from cars.serializers import CarSerializer
from django_filters import rest_framework as filters
from cars.models import Car
from rest_framework import filters as rest_filter


class CarViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):

    serializer_class = CarSerializer
    queryset = Car.objects.all()
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_filter.SearchFilter,
        rest_filter.OrderingFilter,
    )
    # filterset_class = CarFilter
    filterset_fields = ['year', 'make']
    search_fields = ['make']
    ordering_fields = ['year']






