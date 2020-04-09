from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.auth_token.models import Token
from rest_framework.test import APITestCase

from .views import RegistrationAPIView, LoginAPIView, TokenAPIView


class RegistrationAPIViewTestCase(APITestCase):
	
	def set_up(self):
		self.username = 'kailas'
		self.email = 'hiwale.kb@gmail.com'
		self.password = 'kailas123'
		self.user = User.objects.create(self.username, self.email, self.password)
		self.token = Token.objects.create(user=self.user)

		self.api_authentication()


class LoginAPIViewTestCase(APITestCase):
	pass


class TokenAPIViewTestCase(APITestCase):
	pass