from django.urls import path
from user.views import RegistrationAPIView, LoginAPIView, TokenAPIView
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'user'

urlpatterns = [
    path('user/', RegistrationAPIView.as_view(), name="register"),
    path('user/login/', LoginAPIView.as_view(), name="login"),
    path('token/<key>/', TokenAPIView.as_view(), name="token"),
    path('get-token/', obtain_auth_token),
]