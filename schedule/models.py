from django.db import models
from users.models import User
from clients.models import ClientProfile

class Booking(models.Model):
    STATUS_CHOICES = (
        ('scheduled', 'Запланирована'),
        ('completed', 'Проведена'),
        ('cancelled', 'Отменена'),
        ('missed', 'Пропущена'),
    )
    TYPE_CHOICES = (
        ('personal', 'Индивидуальная'),
        ('group', 'Групповая'),
    )
    
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE, related_name='bookings')
    trainer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trainings', limit_choices_to={'role': 'trainer'})
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    booking_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='personal')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['start_time']
    
    def __str__(self):
        return f"{self.client.user.get_full_name()} - {self.trainer.get_full_name()} - {self.start_time}"

class GroupClass(models.Model):
    name = models.CharField(max_length=200)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='group_classes', limit_choices_to={'role': 'trainer'})
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    max_participants = models.IntegerField(default=20)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.name} - {self.instructor.get_full_name()}"
