from django.db import models

class InjuryIncident(models.Model):
    client = models.ForeignKey('clients.ClientProfile', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    description = models.TextField()
    reason = models.CharField(max_length=200)
    
    def __str__(self):
        return f'Инцидент: {self.client.user.get_full_name()} - {self.date}'
