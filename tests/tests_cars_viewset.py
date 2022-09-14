from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from cars.views import CarViewSet
from django.urls import reverse
from cars.models import Car


# Methods -> list, create, retrieve, update, partial_update and destroy


class TestCarsView(APITestCase):

    def test_car_view_set_list(self):
        factory = APIRequestFactory()
        view = CarViewSet.as_view(actions={'get': 'list'})
        car = Car.objects.create(make='AUDI', model='Q7', engine=1.1, year=2001, color='blue')
        car.save()
        request = factory.get(reverse('cars-list'))
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Car.objects.count(), 1)

    def test_car_view_set_create(self):
        factory = APIRequestFactory()
        view = CarViewSet.as_view(actions={'post': 'create'})
        request = factory.post(reverse('cars-list'), {
            'make': 'VW',
            'model': 'Golf',
            'engine': 1.0,
            'year': 2000,
            'color': 'red',
        }, format='json')

        response = view(request)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Car.objects.count(), 1)

    def test_car_view_set_retrieve(self):
        factory = APIRequestFactory()
        view = CarViewSet.as_view(actions={'get': 'retrieve'})
        car = Car.objects.create(make='BMW', model='X7', engine=1.0, year=2000, color='red')
        car.save()
        # basename('cars') + prefix '-detail'
        # request = factory.get(reverse('cars-detail', args=(cat.pk,)))
        request = factory.get(reverse('cars-detail', kwargs={'pk': car.pk}))
        # View functions are called with the request and the arguments from the URL -> (request, pk=cat.pk)
        response = view(request, pk=car.pk)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Car.objects.count(), 1)

    def test_car_view_set_update(self):
        factory = APIRequestFactory()
        car = Car.objects.create(make='Volvo', model='S90', engine=1.0, year=2001, color='red')
        car.save()
        view = CarViewSet.as_view(actions={'put': 'update'})
        request = factory.put(reverse('cars-detail', kwargs={'pk': car.pk}),
                              data={
                                  'make': 'VW',
                                  'model': 'Golf',
                                  'engine': 1.0,
                                  'year': 2000,
                                  'color': 'red',
                              }, format='json')
        response = view(request, pk=car.pk)
        update_car = Car.objects.first()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Car.objects.count(), 1)
        self.assertEqual(update_car.make, 'VW')

    def test_car_view_set_partial_update(self):
        factory = APIRequestFactory()
        car = Car.objects.create(make='Volvo-4', model='S91', engine=1.0, year=2001, color='red')
        car.save()
        view = CarViewSet.as_view(actions={'patch': 'partial_update'})
        request = factory.patch(reverse('cars-detail', kwargs={'pk': car.pk}),
                                data={
                                    'color': 'not_red',
                                }, format='json')
        response = view(request, pk=car.pk)
        update_car = Car.objects.first()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Car.objects.count(), 1)
        self.assertEqual(update_car.color, 'not_red')
