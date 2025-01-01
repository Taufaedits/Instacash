import os
import datetime
import pyotp
from django.core.cache import cache # For rate limiting
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from users.models import User  # Assuming User model is in the users app
from .models import OTPDevice

OTP_LIFETIME = 300  # 5 minutes in seconds
OTP_MAX_ATTEMPTS = 3
OTP_ATTEMPT_WINDOW = 24 * 3600 #24 hours in seconds

class SendOTPView(APIView):
    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        rate_limit_key = f"otp_limit:{email}"
        attempts = cache.get(rate_limit_key, 0)

        if attempts >= OTP_MAX_ATTEMPTS:
            return Response({'error': 'OTP generation limit reached for this email. Try again in 24 hours.'}, status=status.HTTP_429_TOO_MANY_REQUESTS)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'User with this email not found'}, status=status.HTTP_404_NOT_FOUND)

        otp_device, created = OTPDevice.objects.get_or_create(user=user)
        totp = pyotp.TOTP(otp_device.secret, interval=OTP_LIFETIME)
        if created:
            otp_device.secret = totp.secret
            otp_device.save()
        otp = totp.now()

        subject = 'Your OTP for Instacash'
        message = f'Your OTP is: {otp}'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [email]

        try:
            send_mail(subject, message, from_email, recipient_list)
            cache.set(rate_limit_key, attempts + 1, OTP_ATTEMPT_WINDOW) # Increment attempts and set expiration
            return Response({'message': 'OTP sent successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': f'Failed to send email: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)