from django.urls import path, include, re_path
from rest_framework import routers
from .views import BookViewSet, AuthorViewSet, ReviewViewSet, AuthorshipViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    # ... other urlpatterns ...
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'authorships', AuthorshipViewSet)
router.register(r'reviews', ReviewViewSet)



urlpatterns += router.urls