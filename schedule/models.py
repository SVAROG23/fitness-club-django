from django.db import models
from clients.models import ClientProfile

class InjuryIncident(models.Model):
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE, related_name='injuries')
    staff = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, related_name='handled_injuries')
    date = models.DateField(auto_now_add=True)
    description = models.TextField(verbose_name='Описание')
    reason = models.CharField(max_length=200, verbose_name='Причина')
    action_taken = models.TextField(blank=True, verbose_name='Принятые меры')
    
    def __str__(self):
        return f'Инцидент: {self.client.user.get_full_name()} - {self.date}'
    
    class Meta:
        verbose_name = 'Инцидент'
        verbose_name_plural = 'Инциденты'
