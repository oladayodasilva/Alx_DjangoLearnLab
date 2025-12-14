from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path("posts/", include("posts.urls")),
    path('accounts/', include('accounts.urls')),
    path('api/accounts/', include('accounts.urls')),
    path('api/posts/', include('posts.urls')),
    path('api/notifications/', include('notifications.urls')),
    path('api/', include('notifications.urls')),
    path('api/', include('posts.urls')),
    path('api/', include('accounts.urls')),
    path('api/', include('notifications.urls')),
]
