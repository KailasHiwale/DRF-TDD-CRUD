from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.auth_token.models import Token
from rest_framework.test import APITestCase

from .views import InstituteListCreateAPIView, InstituteRetrieveUpdateDestroyAPIView


class InstituteListCreateAPIViewTestCase(APITestCase):
	url = reverse('review:LCInstitute')
	
	def set_up(self):
		self.username = 'kailas'
		self.email = 'hiwale.kb@gmail.com'
		self.password = 'kailas123'
		self.user = User.objects.create(self.username, self.email, self.password)
		self.token = Token.objects.create(user=self.user)

		self.api_authentication()

	def api_authentication(self):
		pass

	def test_create_institute(self):
		pass

	def test_list_institute(self):
		pass



class InstituteRetrieveUpdateDestroyAPIViewTestCase(APITestCase):
	pass
