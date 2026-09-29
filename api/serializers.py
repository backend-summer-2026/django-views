from rest_framework import serializers


class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=False, default=None)
    password = serializers.CharField(required=True)
    confirm = serializers.CharField(required=True)
