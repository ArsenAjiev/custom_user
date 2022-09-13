from rest_framework import serializers
from dealers.models import DealerProfile, DealerCar, TransactionToShowroom
from showrooms.serializers import ShowroomProfileSerializer
from cars.serializers import CarSerializer


class DealerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealerProfile
        fields = '__all__'


class DealerCarSerializer(serializers.ModelSerializer):

    car = CarSerializer(read_only=True)
    dealer = DealerProfileSerializer(read_only=True)

    class Meta:
        model = DealerCar
        fields = [
            'pk',
            'car',
            'dealer',
            'count',
            'price',
        ]


class TransactionToShowroomSerializer(serializers.ModelSerializer):

    car = CarSerializer(read_only=True)
    showroom = ShowroomProfileSerializer(read_only=True)
    dealer = DealerProfileSerializer(read_only=True)

    class Meta:
        model = TransactionToShowroom
        fields = [
            'pk',
            'car',
            'showroom',
            'dealer',
            'price',
            'count',
        ]
