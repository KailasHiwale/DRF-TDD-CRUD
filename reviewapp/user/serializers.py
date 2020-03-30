from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from rest_framework.authtoken.models import Token


class RegistrationSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	confirm_password = serializers.CharField(write_only=True)

	class Meta:
		model = User
		fields = ('id', 'username', 'email', 'password', 'confirm_password', 'date_joined')

	def validate(self, attrs):
		if attrs.get('password') != attrs.get('confirm_password'):
			raise serializers.ValidationError('Password does not matched.')
		del attrs['confirm_password']
		agrs['password'] = make_password(attrs['password'])
		return attrs


class LoginSerializer(serializers.Serializer):
	username = serializers.CharField(required=True)
	password = serializers.CharField(required=True)

	default_error_message = {
	'inactive_account': _('User account is deactivated.'),
	'invalid_credentials': _('Not able to login with given credentials.'), }

	def __init__(self, *args, **kwargs):
		super(LoginSerializer, self).__init__(*args, **kwargs)
		self.User = None

	def validate(self, attrs):
		self.user = authenticate(username=attrs.get('username'), password=attrs.get('password'))
		if self.user:
			if not self.user.is_active:
				raise serializers.ValidationError(self.error_messages['inactive account'])
			return attrs
		else:
			raise serializers.ValidationError(self.error_messages['invalid credentials'])


class TokenSerializer(serializers.ModelSerializer):
	auth_token = serializers.CharField(source='key')

	class Meta:
		model = Token
		fields = ('auth_token', 'created')