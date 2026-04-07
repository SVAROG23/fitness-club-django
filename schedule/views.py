from rest_framework import viewsets, permissions
from .models import Booking, GroupClass
from .serializers import BookingSerializer, GroupClassSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and user.role == 'trainer':
            return Booking.objects.filter(trainer=user)
        elif user.is_authenticated and user.role == 'client':
            return Booking.objects.filter(client__user=user)
        return Booking.objects.all()

class GroupClassViewSet(viewsets.ModelViewSet):
    queryset = GroupClass.objects.all()
    serializer_class = GroupClassSerializer
    permission_classes = [permissions.AllowAny]
