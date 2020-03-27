from django.urls import path, re_path

from .views import InstituteAPIView, ReviewAPIView, ReviewerAPIView


urlpatterns = [
	path('institute/', InstituteAPIView.as_view(), name='get_delete_update_institute'),
	path('institute/<int:pk>/', InstituteAPIView.as_view(), name='getall_create_institute'),

	path('review/', ReviewAPIView.as_view(), name='get_delete_update_review'),
	path('review/<int:pk>/', ReviewAPIView.as_view(), name='getall_create_review'),

	path('reviewer/', ReviewerAPIView.as_view(), name='get_delete_update_reviewer'),
	path('reviewer/<int:pk>/', ReviewerAPIView.as_view(), name='getall_create_reviewer'),
]