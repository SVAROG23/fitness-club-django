from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import MuscleGroup, Exercise, WorkoutProgram, Workout, WorkoutExercise, SetResult
from .serializers import MuscleGroupSerializer, ExerciseSerializer, WorkoutProgramSerializer, WorkoutSerializer, WorkoutExerciseSerializer, SetResultSerializer

class MuscleGroupViewSet(viewsets.ModelViewSet):
    queryset = MuscleGroup.objects.all()
    serializer_class = MuscleGroupSerializer
    permission_classes = [permissions.AllowAny]

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [permissions.AllowAny]

class WorkoutProgramViewSet(viewsets.ModelViewSet):
    queryset = WorkoutProgram.objects.all()
    serializer_class = WorkoutProgramSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and user.role == 'trainer':
            return WorkoutProgram.objects.filter(author=user)
        elif user.is_authenticated and user.role == 'client':
            return WorkoutProgram.objects.filter(client__user=user)
        return WorkoutProgram.objects.all()

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [permissions.AllowAny]

class WorkoutExerciseViewSet(viewsets.ModelViewSet):
    queryset = WorkoutExercise.objects.all()
    serializer_class = WorkoutExerciseSerializer
    permission_classes = [permissions.AllowAny]
    
    @action(detail=True, methods=['post'])
    def add_set_result(self, request, pk=None):
        workout_exercise = self.get_object()
        set_number = request.data.get('set_number')
        weight = request.data.get('weight')
        reps = request.data.get('reps')
        
        set_result = SetResult.objects.create(
            workout_exercise=workout_exercise,
            set_number=set_number,
            weight=weight,
            reps=reps
        )
        return Response(SetResultSerializer(set_result).data)
