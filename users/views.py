from rest_framework.response import Response
import requests
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from django.db.models import Count

from users.serializers import UserSerializer
from users.models import User
from showrooms.models import ShowroomProfile, TransactionToCustomer


class UsersViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @action(detail=False, methods=['get'], url_path='user-test')
    def user_test(self, request):
        count = User.objects.all().count()
        content = {'user': count}
        return Response(content)

    @action(detail=False, methods=["get"], url_path=r"activate/(?P<uid>[\w-]+)/(?P<token>[\w-]+)")
    def activate_account(self, request, uid, token):
        protocol = "https://" if request.is_secure() else "http://"
        web_url = protocol + request.get_host()
        post_url = web_url + "/auth/users/activation/"
        post_data = {"uid": uid, "token": token}
        result = requests.post(post_url, data=post_data)
        content = "Registration completed"
        return Response(content)

    @action(detail=False, methods=['get'], url_path='showroom-stat')
    def showroom_stat(self, request):
        if not request.user.pk or request.user.is_superuser:
            return Response({'Message': "Need authorization as showroom"})
        else:
            # showroom instance
            showroom = ShowroomProfile.objects.get(owner__id=request.user.pk)
            # showroom_profile instance
            query = TransactionToCustomer.objects.filter(showroom_id=showroom)
            # car count
            q = query.values('customer_id').annotate(total_cars=Count('id'))
            content = {'customers': q}
            return Response(content)
