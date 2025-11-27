from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Book
from .serializers import BookSerializer
# ------------------------------------------------------
# BOOK LIST VIEW  (GET): Anyone can view books
# ------------------------------------------------------
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filtering, searching, ordering
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]

    # Filter fields → /books/?author=1&publication_year=2020
    filterset_fields = ['title', 'author', 'publication_year']

    # Search fields → /books/?search=harry
    search_fields = ['title', 'author__name']

    # Order results → /books/?ordering=title  OR  ?ordering=-publication_year
    ordering_fields = ['title', 'publication_year']



# ------------------------------------------------------
# BOOK DETAIL VIEW (GET): Anyone can view a single book
# ------------------------------------------------------
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# ------------------------------------------------------
# BOOK CREATE VIEW (POST): Only authenticated can create
# ------------------------------------------------------
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    # Extra validation handled automatically by serializer
    # but you can override perform_create() if needed:
    # def perform_create(self, serializer):
    #     serializer.save()


# ------------------------------------------------------
# BOOK UPDATE VIEW (PUT/PATCH): Only authenticated users
# ------------------------------------------------------
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    # Custom update logic can go here
    # def perform_update(self, serializer):
    #     serializer.save()


# ------------------------------------------------------
# BOOK DELETE VIEW (DELETE): Only authenticated users
# ------------------------------------------------------
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

