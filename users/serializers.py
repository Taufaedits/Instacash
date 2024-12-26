from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User
from tiers.models import Tier
from tiers.serializers import TierSerializer

class UserSerializer(serializers.ModelSerializer):
    tier = TierSerializer(read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'balance', 'referral_code', 'tier')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return User.objects.create(**validated_data)