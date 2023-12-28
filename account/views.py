from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.authentication import SessionAuthentication
from rest_framework import permissions


# Create your views here.
class UserRegistration(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        if username is None or password is None:
            return Response({"Error": "Fields are required"})

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username is already taken.'})

        user = User.objects.create_user(username=username)
        user.set_password(password)
        user.save()

        serializer = UserSerializer(user)

        filtered_data = {
            'username': serializer.data.get('username'),
            'password': serializer.data.get('password')
        }
        return Response(filtered_data, status=status.HTTP_201_CREATED)


class Login(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        if request.user.is_authenticated:
            return Response({"message": "User is already logged in"}, status=status.HTTP_200_OK)
        data = request.data
        if not data:
            return Response({"Error":"Fields are required"})
        username = data['username']
        password = data['password']

        user = User.objects.filter(username=username).first()
        if not user:
            return Response({"Error": "Invalid username or password"})

        valid_user = authenticate(username=username, password=password)
        if valid_user is None:
            return Response({"Error": "Wrong Credentials"})

        login(user=user, request=request)

        return Response({"Message": "User is Logged in"}, status=status.HTTP_200_OK)


class Logout(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request=request)
        return Response({
            "message": "user is logged out"
        }, status=status.HTTP_200_OK)
