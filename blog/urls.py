from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import Postmvs, Authormvs

router = DefaultRouter()

router.register("post", Postmvs, "post_mvs")
router.register("author", Authormvs, "author_mvs")

urlpatterns = [ ] + router.urls