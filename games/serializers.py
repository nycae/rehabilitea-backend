from rest_framework import serializers

from . import models


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Game
        exclude = ('deleted_at', 'created_at', 'updated_at', 'difficulties')


class DifficultySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Difficulty
        exclude = ('deleted_at', 'created_at', 'updated_at', 'games')
