from rest_framework import serializers
from customers.models import CustomerProfile, CustomerCar
from cars.serializers import CarSerializer
from showrooms.serializers import ShowroomProfileSerializer


class CustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerProfile
        fields = '__all__'


class CustomerCarSerializer(serializers.ModelSerializer):

    car = CarSerializer(read_only=True)
    customer = CustomerProfileSerializer(read_only=True)
    showroom = ShowroomProfileSerializer(read_only=True)

    class Meta:
        model = CustomerCar
        fields = [
            'pk',
            'car',
            'customer',
            'showroom',
            'count',
            'price',
        ]