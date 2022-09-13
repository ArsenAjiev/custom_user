from rest_framework import mixins, viewsets
from customers.models import CustomerProfile, CustomerCar
from customers.serializers import CustomerProfileSerializer, CustomerCarSerializer


class CustomerProfileViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):
    serializer_class = CustomerProfileSerializer
    queryset = CustomerProfile.objects.all()


class CustomerCarViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):
    serializer_class = CustomerCarSerializer
    queryset = CustomerCar.objects.all()