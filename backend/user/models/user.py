from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.CharField(max_length=16, blank=True, null=True, verbose_name='Телефон')
    birthdate = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='Дата рождения', blank=True, null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        default_related_name = 'users'
