from rest_framework import serializers
from django_countries.serializer_fields import CountryField
from showrooms.models import ShowroomProfile, ShowroomCar, TransactionToCustomer
from cars.serializers import CarSerializer
from users.serializers import UserSerializer


class ShowroomProfileSerializer(serializers.ModelSerializer):

    owner = UserSerializer(read_only=True)
    location = CountryField()

    class Meta:
        model = ShowroomProfile
        fields = '__all__'


class ShowroomCarSerializer(serializers.ModelSerializer):
    car = CarSerializer(read_only=True)
    showroom = ShowroomProfileSerializer(read_only=True)

    class Meta:
        model = ShowroomCar
        fields = [
            'pk',
            'car',
            'showroom',
            'price',
            'count',
        ]


class TransactionToCustomerSerializer(serializers.ModelSerializer):
    car = CarSerializer(read_only=True)
    showroom = ShowroomProfileSerializer(read_only=True)

    class Meta:
        model = TransactionToCustomer
        fields = [
            'pk',
            'car',
            'customer',
            'showroom',
            'price',
            'count',
        ]
