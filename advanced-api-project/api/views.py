from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializer
from django.views.generic import ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'


class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'description', 'publication_date', 'author']
    template_name = 'book_form.html'
    success_url = reverse_lazy('book-list')


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('book-list')

class BlogPostListCreateView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

# Custom action to "like" a post
from rest_framework.views import APIView

class LikeBlogPostView(APIView):
    def post(self, request, pk):
        blog = BlogPost.objects.get(pk=pk)
        blog.likes += 1
        blog.save()
        return Response({'status': 'liked', 'likes': blog.likes})

