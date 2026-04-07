from rest_framework import serializers
from .models import MuscleGroup, Exercise, WorkoutProgram, Workout, WorkoutExercise, SetResult

class MuscleGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MuscleGroup
        fields = '__all__'

class ExerciseSerializer(serializers.ModelSerializer):
    muscle_group_name = serializers.CharField(source='muscle_group.name', read_only=True)
    
    class Meta:
        model = Exercise
        fields = '__all__'

class SetResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = SetResult
        fields = '__all__'

class WorkoutExerciseSerializer(serializers.ModelSerializer):
    exercise_name = serializers.CharField(source='exercise.name', read_only=True)
    sets = SetResultSerializer(many=True, read_only=True)
    
    class Meta:
        model = WorkoutExercise
        fields = '__all__'

class WorkoutSerializer(serializers.ModelSerializer):
    exercises = WorkoutExerciseSerializer(many=True, read_only=True)
    
    class Meta:
        model = Workout
        fields = '__all__'

class WorkoutProgramSerializer(serializers.ModelSerializer):
    workouts = WorkoutSerializer(many=True, read_only=True)
    client_name = serializers.CharField(source='client.user.get_full_name', read_only=True)
    author_name = serializers.CharField(source='author.get_full_name', read_only=True)
    
    class Meta:
        model = WorkoutProgram
        fields = '__all__'
