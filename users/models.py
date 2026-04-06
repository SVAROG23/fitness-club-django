from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Администратор'),
        ('trainer', 'Тренер'),
        ('client', 'Клиент'),
        ('manager', 'Руководитель'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='client', verbose_name='Роль')
    phone = models.CharField(max_length=20, blank=True, verbose_name='Телефон')
    
    def __str__(self):
        return f'{self.get_full_name()} ({self.get_role_display()})'
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
