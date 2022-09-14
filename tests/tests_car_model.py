from django.test import TestCase
from cars.models import Car


class TestCarModel(TestCase):
    def setUp(self):
        Car.objects.create(
            make='VW',
            model='Golf',
            engine=1.0,
            year=2000,
            color='red')

    def test_create_car(self):
        car = Car.objects.get(make='VW')
        self.assertEqual(car.make, 'VW')
        self.assertEqual(Car.objects.count(), 1)

    def test_delete_car(self):
        car = Car.objects.get(make='VW')
        car.delete()
        car_model = Car.objects.all()
        self.assertQuerysetEqual(car_model, [])
        self.assertEqual(Car.objects.count(), 0)
