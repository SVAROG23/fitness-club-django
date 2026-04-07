from rest_framework import serializers
from users.serializers import UserSerializer
from .models import ClientProfile, Anthropometry

class AnthropometrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Anthropometry
        fields = '__all__'

class ClientProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    trainer_name = serializers.CharField(source='trainer.get_full_name', read_only=True)
    
    class Meta:
        model = ClientProfile
        fields = '__all__'
