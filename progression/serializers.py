from rest_framework import serializers

from games.serializers import GameSerializer, DifficultySerializer

from . import models


class ProgressionSerializerIn(serializers.ModelSerializer):
    class Meta:
        model = models.Progression
        exclude = ('deleted_at', 'created_at', 'updated_at')


class ProgressionSerializerOut(serializers.ModelSerializer):
    game = GameSerializer()
    difficulty = DifficultySerializer()

    class Meta:
        model = models.Progression
        exclude = ('deleted_at', 'created_at', 'updated_at')
