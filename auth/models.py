from django.db import models
from django.conf import settings

class OTPDevice(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='otp_devices')
    secret = models.CharField(max_length=255)  # Store the OTP secret (base32 encoded)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"OTP Device for {self.user.username}"