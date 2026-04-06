from django.db import models
from django.conf import settings

class ClientProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='client_profile')
    trainer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='clients', limit_choices_to={'role': 'trainer'})
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    gender = models.CharField(max_length=10, choices=[('M', 'Мужской'), ('F', 'Женский')], blank=True, verbose_name='Пол')
    height = models.IntegerField(null=True, blank=True, verbose_name='Рост (см)')
    goals = models.TextField(blank=True, verbose_name='Цели тренировок')
    medical_restrictions = models.TextField(blank=True, verbose_name='Медицинские ограничения')
    
    def __str__(self):
        return f'Профиль: {self.user.get_full_name()}'
    
    class Meta:
        verbose_name = 'Профиль клиента'
        verbose_name_plural = 'Профили клиентов'

class AnthropometryHistory(models.Model):
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE, related_name='anthropometry')
    date = models.DateField(auto_now_add=True, verbose_name='Дата замера')
    weight = models.FloatField(verbose_name='Вес (кг)')
    chest_volume = models.FloatField(null=True, blank=True, verbose_name='Объем груди')
    waist_volume = models.FloatField(null=True, blank=True, verbose_name='Объем талии')
    
    def __str__(self):
        return f'{self.client.user.get_full_name()} - {self.date}'
    
    class Meta:
        verbose_name = 'История антропометрии'
        verbose_name_plural = 'История антропометрии'
        ordering = ['-date']
