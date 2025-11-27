from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializer

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

