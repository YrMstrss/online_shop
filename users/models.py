from django.contrib.auth.models import AbstractUser

from users.managers import UserManager


class User(AbstractUser):

    objects = UserManager()

    def __str__(self):
        return f'{self.username} ({self.first_name} {self.last_name})'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
