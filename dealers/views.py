from rest_framework import mixins, viewsets
from dealers.models import DealerProfile, DealerCar, TransactionToShowroom
from dealers.serializers import DealerProfileSerializer, DealerCarSerializer, TransactionToShowroomSerializer


class DealerProfileViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = DealerProfileSerializer
    queryset = DealerProfile.objects.all()


class DealerCarViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = DealerCarSerializer
    queryset = DealerCar.objects.all()


class TransactionToShowroomViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = TransactionToShowroomSerializer
    queryset = TransactionToShowroom.objects.all()