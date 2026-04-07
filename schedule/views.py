from rest_framework import viewsets, permissions
from django.db.models import Q
from .models import Booking, GroupClass
from .serializers import BookingSerializer, GroupClassSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.role == 'trainer':
            return Booking.objects.filter(trainer=user)
        elif user.role == 'client':
            return Booking.objects.filter(client__user=user)
        return Booking.objects.all()

class GroupClassViewSet(viewsets.ModelViewSet):
    queryset = GroupClass.objects.all()
    serializer_class = GroupClassSerializer
    permission_classes = [permissions.IsAuthenticated]
