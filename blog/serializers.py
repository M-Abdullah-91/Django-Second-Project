from rest_framework import serializers
from .models import PostModel
from .models import AuthorModel


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = "__all__"

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = "__all__"
