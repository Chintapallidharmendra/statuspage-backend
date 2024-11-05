from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import serializers

class LoginSerializer(serializers.ModelSerializer):

    username = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ('username', 'password')

    def validate(self, data):

        user = User.objects.filter(username=data['username']).first()

        if user is None:
            raise serializers.ValidationError('User not found')

        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Incorrect Credentials')
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        existing_user = User.objects.filter(username=validated_data['username']).first()
        if existing_user:
            raise serializers.ValidationError('User already exists')
        user = User.objects.create_user(**validated_data)
        return user
    