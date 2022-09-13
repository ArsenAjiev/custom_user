from rest_framework import mixins, viewsets
from dealers.models import DealerProfile, DealerCar, TransactionToShowroom
from dealers.serializers import DealerProfileSerializer, DealerCarSerializer, TransactionToShowroomSerializer


class DealerProfileViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):
    serializer_class = DealerProfileSerializer
    queryset = DealerProfile.objects.all()



class DealerCarViewSet(viewsets.ModelViewSet):
    queryset = DealerCar.objects.all()
    serializer_class = DealerCarSerializer


class TransactionToShowroomViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = TransactionToShowroomSerializer
    queryset = TransactionToShowroom.objects.all()