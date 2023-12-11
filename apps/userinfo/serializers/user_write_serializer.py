from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class UserWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"