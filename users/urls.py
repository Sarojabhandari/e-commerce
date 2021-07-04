from django.urls import path
from .api import LoginApiView, UserApiView

urlpatterns = [
    path('api/auth/login/', LoginApiView.as_view()),
    path('api/auth/user/', UserApiView.as_view()),
]
