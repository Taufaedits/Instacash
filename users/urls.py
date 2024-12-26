from django.urls import path
from . import views  # Import views from current directory

urlpatterns = [
    path('', views.UserList.as_view(), name='user-list'),
]