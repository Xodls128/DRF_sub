#books/urls.py
from django.urls import path
from .views import BookListCreateAPIView, BookDetailAPIView

urlpatterns = [
    path('', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
]
