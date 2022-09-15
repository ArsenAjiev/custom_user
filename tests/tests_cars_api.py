from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from cars.models import Car
from cars.serializers import CarSerializer


class CarsApiViews(APITestCase):
    def test_get_list(self):
        car = Car.objects.create(
            make='VW',
            model='Golf',
            engine=1.0,
            year=2000,
            color='red')
        url = reverse('cars-list')
        response = self.client.get(url)
        serializer_data = CarSerializer([car], many=True).data
        print(serializer_data)
        print(response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
