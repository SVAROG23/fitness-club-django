from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MuscleGroupViewSet, ExerciseViewSet, WorkoutProgramViewSet, WorkoutViewSet, WorkoutExerciseViewSet

router = DefaultRouter()
router.register(r'muscle-groups', MuscleGroupViewSet)
router.register(r'exercises', ExerciseViewSet)
router.register(r'programs', WorkoutProgramViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'workout-exercises', WorkoutExerciseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
