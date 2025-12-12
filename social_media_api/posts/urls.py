from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedListView
from django.urls import path, include

router = DefaultRouter()
router.register("posts", PostViewSet, basename="posts")

urlpatterns = [
    path("", include(router.urls)),

    path('feed/', FeedListView.as_view(), name='posts-feed'),

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
]

