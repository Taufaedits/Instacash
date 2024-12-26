from django.urls import path
from . import views

urlpatterns = [
    path('', views.TierList.as_view(), name='tier-list'),
    path('<int:pk>/', views.TierDetail.as_view(), name='tier-detail'),
    # ... add other tier-related URLs here ...
]