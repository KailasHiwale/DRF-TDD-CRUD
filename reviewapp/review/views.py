from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Institute
from .serializers import InstituteSerializer


class InstituteAPIView(RetrieveUpdateDestroyAPIView):
	"""Class for get, put, delete API view"""
	
	def get_query(self, pk):
		try:
			institute = Institute.objects.get(pk=pk)
		except Institute.DoesNotExist:
			import pdb;pdb.set_trace()
			return Response({'status': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
		return institute

	def get(self, request, pk):
		institute = self.get_query(pk)
		serializer = InstituteSerializer(institute)
		return Response(serializer.data, status=status.HTTP_200_OK)


	def put(self, request, pk):
		pass


	def delete(self, request, pk):
		pass


# class ReviewAPIView(RetrieveUpdateDestroyAPIView):
# 	"""Class for get, put, delete API view"""
# 	def get(self, request, pk):
# 		pass


# 	def put(self, request, pk):
# 		pass


# 	def delete(self, request, pk):
# 		pass


# class ReviewerAPIView(RetrieveUpdateDestroyAPIView):
# 	"""Class for get, put, delete API view"""
# 	def get(self, request, pk):
# 		pass


# 	def put(self, request, pk):
# 		pass


# 	def delete(self, request, pk):
# 		pass

