from django.urls import path

from .views import InstituteListCreateAPIView, InstituteRetrieveUpdateDestroyAPIView

app_name = 'review'

urlpatterns = [
	path('institute/', InstituteListCreateAPIView.as_view(), name='LCInstitute'),
	path('institute/<int:pk>/', InstituteRetrieveUpdateDestroyAPIView.as_view(), name='RUDInstitute'),
]