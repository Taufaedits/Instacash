from django.urls import path
from users import views  # Import views from users app

urlpatterns = [
    path('', views.UserList.as_view(), name='user-list'),  # List all users
    # ... other URL patterns ...
]