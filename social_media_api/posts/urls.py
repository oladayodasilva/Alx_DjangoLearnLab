from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedListView, FeedView, LikePostView, UnlikePostView
from django.urls import path, include

router = DefaultRouter()
router.register("posts", PostViewSet, basename="posts")

urlpatterns = [
    path("", include(router.urls)),

    path("feed/", FeedView.as_view(), name="feed"),

    # Nested comment routes
    path("posts/<int:post_pk>/comments/", CommentViewSet.as_view({
        "get": "list",
        "post": "create"
    })),
    path("posts/<int:post_pk>/comments/<int:pk>/", CommentViewSet.as_view({
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy"
    })),
    path('posts/<int:pk>/like/', LikePostView.as_view(), name='like-post'),
    path('posts/<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),
]

