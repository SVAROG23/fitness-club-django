from django.db import models
from users.models import User
from clients.models import ClientProfile

class MuscleGroup(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    muscle_group = models.ForeignKey(MuscleGroup, on_delete=models.SET_NULL, null=True)
    video_url = models.URLField(blank=True)
    
    def __str__(self):
        return self.name

class WorkoutProgram(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_programs', limit_choices_to={'role': 'trainer'})
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE, related_name='programs')
    created_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.name} - {self.client.user.get_full_name()}"

class Workout(models.Model):
    STATUS_CHOICES = (
        ('planned', 'Запланирована'),
        ('completed', 'Выполнена'),
        ('missed', 'Пропущена'),
    )
    program = models.ForeignKey(WorkoutProgram, on_delete=models.CASCADE, related_name='workouts')
    name = models.CharField(max_length=200)
    workout_date = models.DateField(null=True, blank=True)
    order_index = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planned')
    
    class Meta:
        ordering = ['order_index', 'workout_date']
    
    def __str__(self):
        return f"{self.name} ({self.get_status_display()})"

class WorkoutExercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='exercises')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets_planned = models.IntegerField(default=3)
    reps_planned = models.IntegerField(default=12)
    weight_planned = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    order_index = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order_index']

class SetResult(models.Model):
    workout_exercise = models.ForeignKey(WorkoutExercise, on_delete=models.CASCADE, related_name='sets')
    set_number = models.IntegerField()
    weight = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    reps = models.IntegerField(null=True, blank=True)
    is_completed = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['set_number']
