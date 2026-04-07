from rest_framework import serializers
from .models import Booking, GroupClass

class BookingSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.user.get_full_name', read_only=True)
    trainer_name = serializers.CharField(source='trainer.get_full_name', read_only=True)
    
    class Meta:
        model = Booking
        fields = '__all__'

class GroupClassSerializer(serializers.ModelSerializer):
    instructor_name = serializers.CharField(source='instructor.get_full_name', read_only=True)
    
    class Meta:
        model = GroupClass
        fields = '__all__'
