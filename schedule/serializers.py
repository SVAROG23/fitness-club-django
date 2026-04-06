from rest_framework import serializers
from .models import InjuryIncident

class InjuryIncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = InjuryIncident
        fields = '__all__'
