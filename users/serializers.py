from django.db import models
from rest_framework import serializers
from django.contrib.auth import authenticate, logout

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user 
        raise serializers.ValidationError("Incorrect Credentials")

