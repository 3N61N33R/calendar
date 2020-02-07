from rest_framework import serializers
from .models import User, CalendarEvents

class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
    class Meta:
        model=User
        fields = ['id','username','email']

class EventSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=CalendarEvents
        fields = ['id','date', 'start_time', 'end_time', 'reason','user']
        