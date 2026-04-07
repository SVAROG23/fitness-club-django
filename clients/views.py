from rest_framework import viewsets, permissions
from users.models import User
from .models import ClientProfile, Anthropometry
from .serializers import ClientProfileSerializer, AnthropometrySerializer

class ClientProfileViewSet(viewsets.ModelViewSet):
    queryset = ClientProfile.objects.all()
    serializer_class = ClientProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.role == 'trainer':
            return ClientProfile.objects.filter(trainer=user)
        elif user.role == 'client':
            return ClientProfile.objects.filter(user=user)
        return ClientProfile.objects.all()

class AnthropometryViewSet(viewsets.ModelViewSet):
    queryset = Anthropometry.objects.all()
    serializer_class = AnthropometrySerializer
    permission_classes = [permissions.IsAuthenticated]
