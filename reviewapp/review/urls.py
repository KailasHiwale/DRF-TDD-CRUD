from django.urls import path, re_path

from .views import InstituteListCreateAPIView, InstituteRetrieveUpdateDestroyAPIView


urlpatterns = [
	path('institute/', InstituteListCreateAPIView.as_view(), name='LCInstitute'),
	path('institute/<int:pk>/', InstituteRetrieveUpdateDestroyAPIView.as_view(), name='RUDInstitute'),

	# path('review/', ReviewAPIView.as_view(), name='get_delete_update_review'),
	# path('review/<int:pk>/', ReviewAPIView.as_view(), name='getall_create_review'),

	# path('reviewer/', ReviewerAPIView.as_view(), name='get_delete_update_reviewer'),
	# path('reviewer/<int:pk>/', ReviewerAPIView.as_view(), name='getall_create_reviewer'),
]