from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings

from rest_framework.routers import DefaultRouter
from rest_framework import permissions

from users.views import UsersViewSet
from cars.views import CarViewSet
from customers.views import CustomerProfileViewSet, CustomerCarViewSet
from dealers.views import DealerProfileViewSet, DealerCarViewSet, TransactionToShowroomViewSet
from showrooms.views import ShowroomProfileViewSet, ShowroomCarViewSet, TransactionToCustomerViewSet
from sales.views import DealerSalesViewSet, ShowroomSalesViewSet

# swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
# user model
router.register('users', UsersViewSet, basename='users')
# car model
router.register('cars', CarViewSet, basename='cars')
# customer model
router.register('customers-profile', CustomerProfileViewSet, basename='customers')
router.register('customer-car', CustomerCarViewSet, basename='customer-car')
# dealer model
router.register('dealers-profile', DealerProfileViewSet, basename='dealers')
router.register('dealer-car', DealerCarViewSet, basename='dealer-car')
router.register('transaction-to-showroom', TransactionToShowroomViewSet, basename='transaction-to-showroom')
# showroom model
router.register('showrooms-profile', ShowroomProfileViewSet, basename='showrooms')
router.register('showroom-car', ShowroomCarViewSet, basename='showroom-car')
router.register('transaction-to-customer', TransactionToCustomerViewSet, basename='transaction-to-customer')
# sales
router.register('showroom-sales', ShowroomSalesViewSet, basename='showroom-sales')
router.register('dealer-sales', DealerSalesViewSet, basename='dealer-sales')


# swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]

urlpatterns += router.urls

# swagger
urlpatterns += [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)