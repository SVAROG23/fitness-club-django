from rest_framework import viewsets
from .models import InjuryIncident
from .serializers import InjuryIncidentSerializer

class InjuryIncidentViewSet(viewsets.ModelViewSet):
    queryset = InjuryIncident.objects.all()
    serializer_class = InjuryIncidentSerializer
