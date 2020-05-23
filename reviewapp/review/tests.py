import json
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.auth_token.models import Token
from rest_framework.test import APITestCase

from .serializer import InstituteSerializer
from .views import InstituteListCreateAPIView, InstituteRetrieveUpdateDestroyAPIView


class InstituteListCreateAPIViewTestCase(APITestCase):
	url = reverse('review:LCInstitute')
	
	def set_up(self):
		self.username = 'kailas'
		self.password = 'kailas123'
		self.email = 'hiwale.kb@gmail.com'
		self.user = User.objects.create(self.username, self.email, self.password)
		self.token = Token.objects.create(user=self.user)

		self.api_authentication()

	def api_authentication(self):
		self.client.credentials(HTTP_AUTHORIZATION='Token' + self.token.key)

	def test_institute_create(self):
		response = self.client.post(self.url, {'institute_name': 'PICT', 'address': 'pune', 'owner': 1})
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_institute_list(self):
		Institute.objects.create(user=self.user, institute_name='PICT', address='pune', owner=1)
		response = self.client.get(self.url)
		self.assertEqual(len(json.loads(response.content)), Institute.objects.count())



class InstituteRetrieveUpdateDestroyAPIViewTestCase(APITestCase):
	url = reverse('review:RUDInstitute')

	def set_up(self):
		self.username = 'kailas'
		self.password = 'kailas123'
		self.email = 'hiwale.kb@gmail.com'
		self.user = User.objects.create_user(self.username, self.email, self.password)
		self.institute = Institute.objects.create(user=self.user, institute_name='PICT', address='pune', owner=1)
		self.token = Token.objects.create(user=self.user)
		self.api_authentication()

	def api_authentication(self):
		self.client.credentials(HTTP_AUTHORIZATION='Token' + self.token.key)

	def test_institute_retrieve(self):
		response = self.client.get(self.url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		institute_serializer_data = InstituteSerializer(instance=self.institute).data
		response_data = json.loads(response.content)
		self.assertEqual(institute_serializer_data, response_data)

	def test_institute_update(self):
		response = self.client.put(self.url, {'institute_name': 'PICTE', 'address': 'Mumbai', 'owner': 1})
		response_data = json.loads(response.content)
		institute = Institute.objects.get(id=self.institute.id)
		self.assertEqual(response_data.get('institute_name'), institute.institute_name)

	def test_institute_partial_update(self):
		response = self.client.patch(self.url, {'address': 'katraj'})
		response_data = json.loads(response.content)
		institute = Institute.objects.get(id=self.institute.id)
		self.assertEqual(response_data.get('address'), institute.address)

	def test_institute_update_with_authorization(self):
		user = User.objects.create_user('Tyrian', 'lanister.tyrian@gmail.com', 'tyrian123')
		token = Token.objects.create(user=user)
		self.client.credentials(HTTP_AUTHORIZATION='Token' + token.key)
		# put
		response = self.client.put(self.url, {'institute_name': 'PICTCOE', 'address': 'South Mumbai', 'owner': 1})
		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

		# patch
		response = self.client.patch(self.url, {'address': 'navi mumbai'})
		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_institute_delete(self):
		response = self.client.delete(self.url)
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

	def test_institute_delete_with_authorization(self):
		user = User.objects.create_user('Tyrian', 'lanister.tyrian@gmail.com', 'tyrian123')
		token = Token.objects.create(user=user)
		self.client.credentials(HTTP_AUTHORIZATION='Token' + token.key)
		# delete
		response = self.client.delete(self.url)
		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)	



