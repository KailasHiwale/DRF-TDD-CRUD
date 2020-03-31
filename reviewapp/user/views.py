from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, GenericAPIView, RetrieveDestroyAPIView

from .serializers import RegistrationSerializer, LoginSerializer, TokenSerializer


class RegistrationAPIView(CreateAPIView):
	serializer_class = RegistrationSerializer

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		user = serializer.instance
		token, created = Token.objects.get_or_create(user=user)
		data = serializer.data
		data['token'] = token.key
		headers = self.get_success_headers(serializer.data)
		
		return Response(data, status=status.HTTP_201_CREATED, headers=headers)


class LoginAPIView(GenericAPIView):
	serializer_class = LoginSerializer

	def post(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		if serializer.is_valid():
			user = serializer.user
			token, _ = Token.objects.get_or_create(user=user)
			return Response(data=TokenSerializer(token).data, status=status.HTTP_200_OK)
		else:
			return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TokenAPIView(RetrieveDestroyAPIView):
	lookup_field = 'key'
	serializer_class = TokenSerializer
	queryset = Token.objects.all()

	def filter(self, queryset):
		return queryset.filter(user=self.request.user)

	def retrieve(self, request, key, *args, **kwargs):
		if key == 'current':
			instance = Token.objects.get(key=request.auth.key)
			serializer = self.get_serializer(instance)
			return Response(serializer.data)
		return super(TokenAPIView, self).retrieve(request, key,  *args, **kwargs)

	def destroy(self, request, key, *args, **kwargs):
		if key == 'current':
			Token.objects.get(key=request.auth.key).delete()
			return Response(status=status.HTTP_204_NO_CONTENT)
		return super(TokenAPIView, self).destroy(request, key, *args, **kwargs)
