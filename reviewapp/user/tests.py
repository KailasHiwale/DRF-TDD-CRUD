from django.test import TestCase
from rest_framework.test import APITestCase

from .views import RegistrationAPIView, LoginAPIView, TokenAPIView


class RegistrationAPIViewTestCase(APITestCase):
	
	def set_up(self):
		self.username = 'kailas'
		self.email = 'hiwale.kb@gmail.com'
		self.password = 'kailas123'
		self.token = 'token'


class LoginAPIViewTestCase(APITestCase):
	pass


class TokenAPIViewTestCase(APITestCase):
	pass