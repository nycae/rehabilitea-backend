from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import GameSerializer
from .models import Game


class GameReadOnlyView(viewsets.ReadOnlyModelViewSet):
    queryset = Game.objects.filter(deleted_at=None).all()
    serializer_class = GameSerializer


@api_view(['GET'])
def get_name_id_by_name(request, name):
    return Response(GameSerializer(Game.objects.filter(name__contains=name).first()).data)
