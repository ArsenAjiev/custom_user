from django.test import TestCase
from users.models import User


class TestCarModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='new_user', email='new_user@test.com', password='top_secret')



