from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        extra_kwargs = {
            'password': {'write_only': True, 'style': {'input_type': 'password'}},
            'user_permissions': {'read_only': True},
            'groups': {'read_only': True},
            'last_login': {'read_only': True},
            'date_joined': {'read_only': True}
        }
        model = User
        fields = [
            'id',
            'last_login',
            'date_joined',
            'username',
            'password',
            'groups',
            'user_permissions',
        ]