from django.urls import path
from .views import BookListView, BookUpdateView, BookDeleteView

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='books')
router.register(r'authors', AuthorViewSet, basename='authors')

urlpatterns = [
    path('books/create/', BookViewSet.as_view({'post': 'create'}), name='books-create'),
    path('books/update/<int:pk>/', BookViewSet.as_view({'put': 'update'}), name='books-update'),
    path('books/delete/<int:pk>/', BookViewSet.as_view({'delete': 'destroy'}), name='books-delete'),
]

urlpatterns += router.urls
