from rest_framework import viewsets
from .models import ClientProfile
from .serializers import ClientProfileSerializer

class ClientProfileViewSet(viewsets.ModelViewSet):
    queryset = ClientProfile.objects.all()
    serializer_class = ClientProfileSerializer
