from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from workouts.models import Workout
from clients.models import ClientProfile
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
def reports_view(request):
    user = request.user
    context = {}
    
    if user.role == 'manager' or user.is_superuser:
        trainers = User.objects.filter(role='trainer')
        trainer_load = []
        for trainer in trainers:
            total_workouts = Workout.objects.filter(
                program__author=trainer,
                status='completed'
            ).count()
            trainer_load.append({
                'name': trainer.get_full_name(),
                'total': total_workouts
            })
        context['trainer_load'] = trainer_load
        context['clients_total'] = ClientProfile.objects.count()
    
    return render(request, 'analytics/reports.html', context)
