from rest_framework import serializers
from .models import InjuryIncident

class InjuryIncidentSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.user.get_full_name', read_only=True)
    trainer_name = serializers.CharField(source='trainer.get_full_name', read_only=True)
    
    class Meta:
        model = InjuryIncident
        fields = '__all__'
