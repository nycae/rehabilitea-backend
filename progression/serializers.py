from rest_framework import serializers

from . import models


class ProgressionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Progression
        fields = ('__all__', )
