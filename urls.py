from django.contrib import admin
from django.urls import path, include  # Import include for handling app urls

urlpatterns = [
    path('admin/', admin.site.urls),  # Include admin URLs
    # ... your app URLs will go here
]