from django.urls import path
from .views import BlogPostListCreateView, BlogPostDetailView, LikeBlogPostView

urlpatterns = [
    path('posts/', BlogPostListCreateView.as_view()),
    path('posts/<int:pk>/', BlogPostDetailView.as_view()),
    path('posts/<int:pk>/like/', LikeBlogPostView.as_view()),
]

