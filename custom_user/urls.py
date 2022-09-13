from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views import UsersViewSet
from cars.views import CarViewSet
from customers.views import CustomerProfileViewSet, CustomerCarViewSet
from dealers.views import DealerProfileViewSet, DealerCarViewSet, TransactionToShowroomViewSet
from showrooms.views import ShowroomProfileViewSet, ShowroomCarViewSet, TransactionToCustomerViewSet

router = DefaultRouter()
# user model
router.register('users', UsersViewSet, basename='users')
# car model
router.register('cars', CarViewSet, basename='cars')
# customer model
router.register('customers', CustomerProfileViewSet, basename='customers')
router.register('customer-car', CustomerCarViewSet, basename='customer-car')
# dealer model
router.register('dealers', DealerProfileViewSet, basename='dealers')
router.register('dealer-car', DealerCarViewSet, basename='dealer-car')
router.register('transaction-to-showroom', TransactionToShowroomViewSet, basename='transaction-to-showroom')
# showroom model
router.register('showrooms', ShowroomProfileViewSet, basename='showrooms')
router.register('showroom-car', ShowroomCarViewSet, basename='showroom-car')
router.register('transaction-to-customer', TransactionToCustomerViewSet, basename='transaction-to-customer')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
]

urlpatterns += router.urls
