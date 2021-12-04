from rest_framework import viewsets

from .serializers import EventSerializer, GameStartSerializer, GameEndedSerializer
from .models import Event, GameStarted, GameEnded


class BaseEventView(viewsets.ModelViewSet):
    queryset = Event.objects.filter(deleted_at=None).all()
    serializer_class = EventSerializer


class GameStartView(viewsets.ModelViewSet):
    queryset = GameStarted.objects.filter(deleted_at=None).all()
    serializer_class = GameStartSerializer


class GameEndView(viewsets.ModelViewSet):
    queryset = GameEnded.objects.filter(deleted_at=None).all()
    serializer_class = GameEndedSerializer
