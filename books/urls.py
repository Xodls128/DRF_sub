#books/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, ReviewViewSet

router = DefaultRouter()
router.register('Books', BookViewSet)
router.register('Reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

