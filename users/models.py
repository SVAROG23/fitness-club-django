from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Администратор'),
        ('trainer', 'Тренер'),
        ('client', 'Клиент'),
        ('manager', 'Руководитель'),
    )
    role = models.CharField('Роль', max_length=20, choices=ROLE_CHOICES, default='client')
    phone = models.CharField('Телефон', max_length=20, blank=True)
    avatar = models.ImageField('Аватар', upload_to='avatars/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.get_full_name() or self.username} ({self.get_role_display()})"
    
    def is_trainer(self):
        return self.role == 'trainer'
    
    def is_client(self):
        return self.role == 'client'
    
    def is_manager(self):
        return self.role == 'manager'
