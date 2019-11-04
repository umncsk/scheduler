from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'user_name',
            'organization',
            'user_schedule',
        )
        model = User
