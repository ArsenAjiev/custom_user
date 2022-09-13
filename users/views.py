from rest_framework.response import Response
import requests
from rest_framework import mixins, viewsets
from rest_framework.decorators import action

from users.serializers import UserSerializer
from users.models import User


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
