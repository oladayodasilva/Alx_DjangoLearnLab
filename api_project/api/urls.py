from django.urls import path,include
from .views import BookList, BookDetail
from .views import BookViewSet 

urlpatterns = [
    path("api/books/", BookList.as_view(), name='book_all'),
    path("api/books/<int:pk>/", BookDetail.as_view(), name="book_detail"),
]
