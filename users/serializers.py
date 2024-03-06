from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from shopping_carts.models import ShoppingCart
from users.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для регистрации пользователя
    """
    password = serializers.CharField(write_only=True, validators=[validate_password])

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        ShoppingCart.objects.create(user=user)
        return user

    class Meta:
        model = User
        fields = ('username', 'password')
