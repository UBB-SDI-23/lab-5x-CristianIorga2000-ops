from django.urls import path, include 
from rest_framework import routers
from .views import BookViewSet, AuthorViewSet, ReviewViewSet, AuthorshipViewSet

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'authorships', AuthorshipViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [ ]


urlpatterns += router.urls