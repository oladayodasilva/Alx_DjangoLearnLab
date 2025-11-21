from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

router = DefaultRouter()
router.register(r'books-viewset', BookViewSet, basename='book-viewset')

urlpatterns = [
    path('books/, BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
]
