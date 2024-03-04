from rest_framework import generics

from users.serializers import UserRegisterSerializer


class RegisterView(generics.CreateAPIView):
    """
    Контроллер для регистрации пользователя
    """
    serializer_class = UserRegisterSerializer
