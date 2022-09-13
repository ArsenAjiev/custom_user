from rest_framework import serializers
from sales.models import ShowroomSales, DealerSales


class ShowroomSalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowroomSales
        fields = '__all__'


class DealerSalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealerSales
        fields = '__all__'
