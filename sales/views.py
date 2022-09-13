from rest_framework import viewsets, mixins
from sales.models import DealerSales, ShowroomSales
from sales.serializers import DealerSalesSerializer, ShowroomSalesSerializer


class DealerSalesViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):
    queryset = DealerSales.objects.all()
    serializer_class = DealerSalesSerializer


class ShowroomSalesViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin
):
    queryset = ShowroomSales.objects.all()
    serializer_class = ShowroomSalesSerializer
