from rest_framework import viewsets

from .serializers import ProgressionSerializer
from .models import Progression


class ProgressionViewSet(viewsets.ModelViewSet):
    queryset = Progression
    serializer_class = ProgressionSerializer
