import pyotp
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from .models import OTPDevice # If you created this model

class SendOTPView(APIView):
    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Check if user exists (you might want to adjust this based on your user model)
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'User with this email not found'}, status=status.HTTP_404_NOT_FOUND)
        
        #Using models to store secrets
        otp_device, created = OTPDevice.objects.get_or_create(user=user)
        totp = pyotp.TOTP(otp_device.secret, interval=300) # 5 minutes validity
        if created:
            otp_device.secret = totp.secret
            otp_device.save()
        otp = totp.now()
        
        # Send OTP via email
        subject = 'Your OTP for Instacash'
        message = f'Your OTP is: {otp}'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [email]

        try:
            send_mail(subject, message, from_email, recipient_list)
            return Response({'message': 'OTP sent successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': f'Failed to send email: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class VerifyOTPView(APIView):
    def post(self, request):
        email = request.data.get('email')
        otp = request.data.get('otp')

        if not email or not otp:
            return Response({'error': 'Email and OTP are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        try:
            otp_device = OTPDevice.objects.get(user=user)
            totp = pyotp.TOTP(otp_device.secret, interval=300)
            if totp.verify(otp):
                return Response({'message': 'OTP verified successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)

        except OTPDevice.DoesNotExist:
            return Response({'error': 'No OTP device found for this user. Request a new OTP'}, status=status.HTTP_404_NOT_FOUND)