from django.test import TestCase
from .models import User

# Create your tests here.
class UserTestCase(TestCase):
    def getAll(self):
        users = User.objects.all()
        print('users')