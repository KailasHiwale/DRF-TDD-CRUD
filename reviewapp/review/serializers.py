from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Institute, Review, Reviewer


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


# class ReviewSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Review
# 		fields = [
# 			'id',
# 			'institute',
# 			'reviewer',
# 			'overall_rating',
# 			'review_title',
# 			'merits',
# 			'demerits',
# 			'advice', ]


# class ReviewerSerializer(serializers.Serializer):
# 	user_id = serializers.IntegerField(required=False, read_only=True)
# 	reviewer_name = serializers.CharField(required=False, max_length=150)
# 	email_id = serializers.EmailField()
# 	profession_status = serializers.CharField(required=False, allow_blank=True, max_length=150)
# 	city = serializers.CharField(required=False, allow_blank=True, max_length=150)
# 	state = serializers.CharField(required=False, allow_blank=True, max_length=150)
# 	country = serializers.CharField(required=False, allow_blank=True, max_length=150, default='India')

# 	class Meta:
# 		model = Reviewer
# 		fields = ('user_id', 'reviewer_name', 'email_id', 'profession_status',
# 				  'city', 'state', 'country')

# 	def create(self, validated_data):
# 		"""Create and return new `Reviewer` instance for validated data"""
# 		return Reviewer.objects.create(**validated_data)

# 	def update(self, instance, validated_data):
# 		"""Update and return an existing `Reviewer` instance for validated data"""
# 		instance.user_id = validated_data.get('user_id', instance.user_id)
# 		instance.reviewer_name = validated_data.get('reviewer_name', instance.reviewer_name)
# 		instance.email_id = validated_data.get('email_id', instance.email_id)
# 		instance.profession_status = validated_data.get('profession_status', instance.profession_status)
# 		instance.city = validated_data.get('city', instance.city)
# 		instance.state = validated_data.get('state', instance.state)
# 		instance.country = validated_data.get('country', instance.country)
# 		instance.save()
# 		return instance

# 	def delete(self, instance):
# 		pass
