from rest_framework import viewsets

from .serializers import GameSerializer
from .models import Game


class GameReadOnlyView(viewsets.ReadOnlyModelViewSet):
    queryset = Game.objects.filter(deleted_at=None).all()
    serializer_class = GameSerializer
