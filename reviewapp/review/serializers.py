from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Institute


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username", "email", "date_joined")


class InstituteSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Institute
		fields = ['id', 'institute_name', 'address', 'pin_code', 'office_mail',
				  'phone_number', 'website', 'institute_type', 'founded_in',
				  'affiliated_to', 'approved_by', 'owner', ]
