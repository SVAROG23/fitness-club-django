from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count, Sum, Q
from django.utils import timezone
from datetime import timedelta
from .models import InjuryIncident
from .serializers import InjuryIncidentSerializer
from workouts.models import Workout
from schedule.models import Booking

class InjuryIncidentViewSet(viewsets.ModelViewSet):
    queryset = InjuryIncident.objects.all()
    serializer_class = InjuryIncidentSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.role == 'trainer':
            return InjuryIncident.objects.filter(trainer=user)
        elif user.role == 'client':
            return InjuryIncident.objects.filter(client__user=user)
        return InjuryIncident.objects.all()

class AnalyticsViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]
    
    @action(detail=False, methods=['get'])
    def trainer_load(self, request):
        """Загрузка тренеров"""
        from users.models import User
        trainers = User.objects.filter(role='trainer')
        result = []
        for trainer in trainers:
            bookings_count = Booking.objects.filter(trainer=trainer, status='scheduled').count()
            result.append({
                'trainer_id': trainer.id,
                'trainer_name': trainer.get_full_name(),
                'bookings_count': bookings_count,
            })
        return Response(result)
    
    @action(detail=False, methods=['get'])
    def client_progress(self, request):
        """Прогресс клиента"""
        user = request.user
        if user.role == 'client':
            from clients.models import Anthropometry
            anthropometry = Anthropometry.objects.filter(client__user=user).order_by('date')
            data = [{'date': a.date, 'weight': float(a.weight)} for a in anthropometry]
            return Response(data)
        return Response({'error': 'Доступно только для клиентов'}, status=403)
    
    @action(detail=False, methods=['get'])
    def injury_stats(self, request):
        """Статистика травматизма"""
        injuries = InjuryIncident.objects.all()
        total = injuries.count()
        by_reason = injuries.values('reason').annotate(count=Count('id'))
        return Response({
            'total': total,
            'by_reason': by_reason,
        })
