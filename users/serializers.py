from rest_framework import serializers
# from .models import CustomUser

# class CustomUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ('id', 'email', 'username', 'is_active', 'is_staff', 'date_joined')
#         read_only_fields = ('id', 'date_joined')

#     def create(self, validated_data):
#         return CustomUser.objects.create_user(**validated_data)

#     def update(self, instance, validated_data):
#         instance.email = validated_data.get('email', instance.email)
#         instance.username = validated_data.get('username', instance.username)
#         instance.is_active = validated_data.get('is_active', instance.is_active)
#         instance.is_staff = validated_data.get('is_staff', instance.is_staff)
#         instance.save()
#         return instance


from django.contrib.auth.models import User
from .models import UserProfile, EmailVerificationToken

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'date_of_birth', 'location', 'bio']
        read_only_fields = ['email']  # Устанавливаем поле email только для чтения


class EmailVerificationTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailVerificationToken
        fields = '__all__'

