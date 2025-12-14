from rest_framework import viewsets, permissions, filters, generics, status
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

User = get_user_model()

class FeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by("-created_at")
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # SAFE methods (GET, HEAD, OPTIONS) allowed for everyone
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only the owner can edit or delete
        return obj.author == request.user


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "content"]

    def perform_create(self, serializer):
        serializer.save(author=self.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("-created_at")
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        post_id = self.kwargs.get("post_pk")
        serializer.save(author=self.request.user, post_id=post_id)

class FeedListView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]   # only for authenticated users
    pagination_class = None  # or your PageNumberPagination from settings

    def get_queryset(self):
        user = self.request.user
        # If using CustomUser.following many-to-many:
        following_qs = user.following.all()
        # If using Profile: following_qs = user.profile.following.all()

        # avoid returning empty QuerySet for no-following users
        if not following_qs.exists():
            return Post.objects.none()

        return Post.objects.filter(author__in=following_qs).order_by("-created_at")


class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)

        like, created = Like.objects.get_or_create(
            user=request.user,
            post=post
        )

        if not created:
            return Response(
                {"detail": "Post already liked"},
                status=status.HTTP_400_BAD_REQUEST
            )

        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb="liked your post",
            target=post
        )

        return Response(
            {"detail": "Post liked"},
            status=status.HTTP_201_CREATED
        )


class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        like = Like.objects.filter(user=request.user, post=post)

        if like.exists():
            like.delete()
            return Response({"detail": "Post unliked"})

        return Response(
            {"detail": "You have not liked this post"},
            status=status.HTTP_400_BAD_REQUEST
        )

