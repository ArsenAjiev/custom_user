from rest_framework import mixins, viewsets
from customers.models import CustomerProfile, CustomerCar
from customers.serializers import CustomerProfileSerializer, CustomerCarSerializer


class CustomerProfileViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = CustomerProfileSerializer
    queryset = CustomerProfile.objects.all()


class CustomerCarViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = CustomerCarSerializer
    queryset = CustomerCar.objects.all()