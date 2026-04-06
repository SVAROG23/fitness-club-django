from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkoutProgramViewSet, WorkoutViewSet, ExerciseViewSet, workout_fix_view

router = DefaultRouter()
router.register(r'programs', WorkoutProgramViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'exercises', ExerciseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('fix/<int:workout_id>/', workout_fix_view, name='workout_fix'),
]
