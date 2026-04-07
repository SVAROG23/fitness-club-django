from django.contrib.auth.models import AbstractUser
from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Администратор'),
        ('trainer', 'Тренер'),
        ('client', 'Клиент'),
        ('manager', 'Руководитель'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='client')
    phone = models.CharField(max_length=20, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.get_full_name()} ({self.get_role_display()})"
