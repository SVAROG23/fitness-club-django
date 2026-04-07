from django.db import models
from users.models import User
from clients.models import ClientProfile
from workouts.models import Workout

class InjuryIncident(models.Model):
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE, related_name='injuries')
    trainer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reported_injuries')
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    reason = models.CharField(max_length=200)
    action_taken = models.TextField(blank=True)
    
    def __str__(self):
        return f"Травма: {self.client.user.get_full_name()} - {self.date.date()}"
