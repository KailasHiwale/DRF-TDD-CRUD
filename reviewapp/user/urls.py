from django.urls import path
from user.views import RegistrationAPIView, LoginAPIView, TokenAPIView

app_name = 'user'

urlpatterns = [
    path('', RegistrationAPIView.as_view(), name="register"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('token/<key>/', TokenAPIView.as_view(), name="token"),
]