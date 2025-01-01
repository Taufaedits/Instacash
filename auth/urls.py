from django.urls import path
from . import views

urlpatterns = [
    path('send_otp/', views.SendOTPView.as_view(), name='send_otp'),
    path('verify_otp/', views.VerifyOTPView.as_view(), name='verify_otp'),
]