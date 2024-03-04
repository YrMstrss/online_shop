from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    def __str__(self):
        return f'{self.username} ({self.first_name} {self.last_name})'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
