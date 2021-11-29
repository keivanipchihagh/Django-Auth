from django.urls import path
from .views import *

urlpatterns = [
    path(route = 'login/', view = LoginView.as_view(), name = 'login'),
    path(route = 'register/', view = RegisterApi.as_view(), name = 'register'),
]