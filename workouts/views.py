from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .models import Workout, WorkoutProgram, Exercise
from .serializers import WorkoutSerializer, WorkoutProgramSerializer, ExerciseSerializer

class WorkoutProgramViewSet(viewsets.ModelViewSet):
    queryset = WorkoutProgram.objects.all()
    serializer_class = WorkoutProgramSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

@login_required
def workout_fix_view(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id)
    workout_exercises = workout.exercises.all().order_by('order_index')
    
    context = {
        'workout': workout,
        'exercises': workout_exercises,
    }
    return render(request, 'workouts/workout_fix.html', context)
