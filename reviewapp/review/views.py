from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Institute
from .serializers import InstituteSerializer
from .permissions import IsOwnerOrReadOnly	#, IsAuthenticated


class InstituteListCreateAPIView(ListCreateAPIView):
	"""Class for get, put, delete API view"""
	serializer_class = InstituteSerializer

	def get_queryset(self):
		return Institute.objects.filter(owner=self.request.user)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class InstituteRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
	"""Class for get, put, delete API view"""
	serializer_class = InstituteSerializer
	queryset = Institute.objects.all()
	permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

