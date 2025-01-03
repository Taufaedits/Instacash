from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/tiers/', include('tiers.urls')),
    path('api/auth/', include('auth.urls')), # Include auth urls
    path('api-auth/', include('rest_framework.urls')),
]