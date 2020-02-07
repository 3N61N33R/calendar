from django.shortcuts import render
from rest_framework.viewsets import  ModelViewSet
from .models import  User, CalendarEvents
from .serializers import UserSerializer, EventSerializer

# Create your views here.
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class EventsViewSet(ModelViewSet):
    queryset = CalendarEvents.objects.all()
    serializer_class = EventSerializer

    
