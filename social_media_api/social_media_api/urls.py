from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path("posts/", include("posts.urls")),
    path('accounts/', include('accounts.urls')),
    path('api/', include('api.urls')),
    path('api/', include('notifications.urls')),
]
