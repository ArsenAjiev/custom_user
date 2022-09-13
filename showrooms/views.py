from rest_framework import mixins, viewsets
from showrooms.models import ShowroomProfile, ShowroomCar, TransactionToCustomer
from showrooms.serializers import ShowroomProfileSerializer, ShowroomCarSerializer, TransactionToCustomerSerializer


class ShowroomProfileViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = ShowroomProfileSerializer
    queryset = ShowroomProfile.objects.all()


class ShowroomCarViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = ShowroomCarSerializer
    queryset = ShowroomCar.objects.all()


class TransactionToCustomerViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = TransactionToCustomerSerializer
    queryset = TransactionToCustomer.objects.all()