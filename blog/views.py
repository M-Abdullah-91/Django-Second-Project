from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import permissions
from .models import PostModel, AuthorModel
from .serializers import PostSerializer, AuthorSerializer


class ViewSetPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_authenticated:
            if view.action == "list":
                return True
            elif view.action in ["create", "update", "partial_update", "destroy"] and obj.created_by == request.user:
                return True
        return False


# Create your views here.

class Postmvs(viewsets.ModelViewSet):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [ViewSetPermissions]



class Authormvs(viewsets.ModelViewSet):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()
