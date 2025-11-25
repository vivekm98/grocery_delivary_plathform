from django.contrib.auth.models import User
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,min_length=8)
    class Meta:
        model = User
        fields = ['email','password']

    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email':'Email already exist.'})
        base_username =email.split('@')[0]
        username = base_username
        counter = 1
        while User.objects.filter(username=username).exists():
            username = f"{base_username}{counter}"
            counter += 1

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()