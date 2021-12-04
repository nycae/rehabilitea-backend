from rest_framework import response
from rest_framework import viewsets
from rest_framework import exceptions

from .serializers import ProgressionSerializerOut, ProgressionSerializerIn
from .models import Progression


class ProgressionView(viewsets.ModelViewSet):
    queryset = Progression.objects.filter(deleted_at=None).order_by(
        '-difficulty__order')
    serializer_class = ProgressionSerializerIn

    def list(self, request, user_id=0, game_name=''):
        queryset = Progression.objects.filter(
            deleted_at=None,
            user__id=user_id,
            game__name=game_name
        ).order_by(
            '-difficulty__order'
        ).first()
        serializer = ProgressionSerializerOut(queryset)
        return response.Response(data=serializer.data)

    def update(self, request, *args, **kwargs):
        raise exceptions.MethodNotAllowed
