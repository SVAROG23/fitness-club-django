from django.db import models
from users.models import User

class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client_profile')
    trainer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='clients', limit_choices_to={'role': 'trainer'})
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=(('M', 'Мужской'), ('F', 'Женский')), blank=True)
    height = models.IntegerField(null=True, blank=True, help_text='Рост в см')
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    goals = models.TextField(blank=True, help_text='Цели тренировок')
    medical_restrictions = models.TextField(blank=True, help_text='Медицинские ограничения')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Профиль клиента: {self.user.get_full_name()}"

class Anthropometry(models.Model):
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE, related_name='anthropometry')
    date = models.DateField(auto_now_add=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, help_text='Вес в кг')
    chest = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, help_text='Грудь в см')
    waist = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, help_text='Талия в см')
    hips = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, help_text='Бедра в см')
    
    class Meta:
        ordering = ['-date']
