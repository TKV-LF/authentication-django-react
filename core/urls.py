from django.urls import path
from .views import RegisterAPIView, LoginAPIView, UserAPIView, RefreshTokenAPIView, LogoutAPIView
urlpatterns = [
    path('register', RegisterAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('user', UserAPIView.as_view()),
    path('refresh', RefreshTokenAPIView.as_view()),
    path('logout', LogoutAPIView.as_view()),
]
