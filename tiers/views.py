# tiers/views.py
from rest_framework import generics, permissions
from .models import Tier
from .serializers import TierSerializer

class TierList(generics.ListAPIView):
    queryset = Tier.objects.all()
    serializer_class = TierSerializer
    permission_classes = (permissions.AllowAny,)  # Allow anyone to view tiers

class TierDetail(generics.RetrieveAPIView):
    queryset = Tier.objects.all()
    serializer_class = TierSerializer
    permission_classes = (permissions.AllowAny,)