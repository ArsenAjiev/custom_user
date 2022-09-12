from users.views import UsersViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('users', UsersViewSet, basename='activation')

urlpatterns = []
urlpatterns += router.urls
