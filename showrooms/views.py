from rest_framework import mixins, viewsets
from showrooms.models import ShowroomProfile, ShowroomCar, TransactionToCustomer
from showrooms.serializers import ShowroomProfileSerializer, ShowroomCarSerializer, TransactionToCustomerSerializer


class ShowroomProfileViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):
    serializer_class = ShowroomProfileSerializer
    queryset = ShowroomProfile.objects.all()


class ShowroomCarViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
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