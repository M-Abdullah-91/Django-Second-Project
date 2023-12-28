from django.contrib import admin
from django.urls import path
from .views import UserRegistration
from .views import Login
from .views import Logout

urlpatterns = [
    path('register', UserRegistration.as_view(), name='user-registration'),
    path('login', Login.as_view(), name='user-login'),
    path('logout', Logout.as_view(), name='user-logout'),
]