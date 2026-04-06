from django.db import models
from django.conf import settings
from clients.models import ClientProfile

class Exercise(models.Model):
    MUSCLE_GROUPS = [
        ('chest', 'Грудные'),
        ('back', 'Спина'),
        ('legs', 'Ноги'),
        ('shoulders', 'Плечи'),
        ('arms', 'Руки'),
        ('abs', 'Пресс'),
        ('cardio', 'Кардио'),
    ]
    name = models.CharField(max_length=100, verbose_name='Название упражнения')
    description = models.TextField(verbose_name='Описание техники')
    muscle_group = models.CharField(max_length=20, choices=MUSCLE_GROUPS, verbose_name='Группа мышц')
    video_url = models.URLField(blank=True, verbose_name='Ссылка на видео')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Упражнение'
        verbose_name_plural = 'Упражнения'

class WorkoutProgram(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название программы')
    description = models.TextField(blank=True, verbose_name='Описание')
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE, related_name='programs', verbose_name='Клиент')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_programs', verbose_name='Автор (тренер)')
    created_date = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    is_active = models.BooleanField(default=True, verbose_name='Активна')
    
    def __str__(self):
        return f'{self.name} - {self.client.user.get_full_name()}'
    
    class Meta:
        verbose_name = 'Программа тренировок'
        verbose_name_plural = 'Программы тренировок'

class Workout(models.Model):
    STATUS_CHOICES = [
        ('planned', 'Запланирована'),
        ('in_progress', 'В процессе'),
        ('completed', 'Завершена'),
        ('cancelled', 'Отменена'),
    ]
    program = models.ForeignKey(WorkoutProgram, on_delete=models.CASCADE, related_name='workouts', verbose_name='Программа')
    name = models.CharField(max_length=100, verbose_name='Название тренировки')
    workout_date = models.DateField(verbose_name='Дата тренировки')
    order_index = models.IntegerField(default=0, verbose_name='Порядковый номер')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planned', verbose_name='Статус')
    feeling = models.IntegerField(null=True, blank=True, verbose_name='Самочувствие (1-5)')
    
    def __str__(self):
        return f'{self.name} ({self.workout_date})'
    
    class Meta:
        verbose_name = 'Тренировка'
        verbose_name_plural = 'Тренировки'
        ordering = ['workout_date', 'order_index']

class WorkoutExercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='exercises', verbose_name='Тренировка')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, verbose_name='Упражнение')
    sets_planned = models.IntegerField(default=3, verbose_name='Плановое количество подходов')
    reps_planned = models.IntegerField(default=10, verbose_name='Плановое количество повторений')
    order_index = models.IntegerField(default=0, verbose_name='Порядковый номер')
    
    def __str__(self):
        return f'{self.workout.name} - {self.exercise.name}'
    
    class Meta:
        verbose_name = 'Упражнение тренировки'
        verbose_name_plural = 'Упражнения тренировок'

class Set(models.Model):
    workout_exercise = models.ForeignKey(WorkoutExercise, on_delete=models.CASCADE, related_name='sets', verbose_name='Упражнение в тренировке')
    set_number = models.IntegerField(verbose_name='Номер подхода')
    weight_kg = models.FloatField(default=0, verbose_name='Вес (кг)')
    reps_done = models.IntegerField(default=0, verbose_name='Выполнено повторений')
    is_completed = models.BooleanField(default=False, verbose_name='Выполнен')
    
    def __str__(self):
        return f'Подход {self.set_number}: {self.weight_kg}кг × {self.reps_done}'
    
    class Meta:
        verbose_name = 'Подход'
        verbose_name_plural = 'Подходы'
