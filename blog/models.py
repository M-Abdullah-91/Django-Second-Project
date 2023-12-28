from django.db import models
from django.contrib.auth.models import User


class AuthorModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    first_name = models.CharField(max_length=200, default="")
    last_name = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.first_name +" "+ self.last_name
class PostModel(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
