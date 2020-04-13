from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.auth_token.models import Token
from rest_framework.test import APITestCase

from .views import RegistrationAPIView, LoginAPIView, TokenAPIView


class RegistrationAPIViewTestCase(APITestCase):
	url = reverse('user:register')
	
	def test_invalid_password(self):
		pass

	def test_user_registration(self):
		pass

	def test_validate_unique_username(self):
		pass


class LoginAPIViewTestCase(APITestCase):
	url = reverse('user:login')

	def test_without_password_authentication(self):
		pass

	def test_with_password_authentication(self):
		pass

	def test_with_valid_credentials(self):
		pass


class TokenAPIViewTestCase(APITestCase):
	def url(self):
		pass

	def set_up(self):
		pass

	def delete_user_and_token(self):
		pass

	def api_authentication(self):
		pass

	def test_delete_using_key(self):
		pass

	def test_delete_current(self):
		pass

	def test_delete_unauthorized(self):
		pass

	def test_get(self):
		pass