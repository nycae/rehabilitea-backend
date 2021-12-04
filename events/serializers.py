from rest_framework import serializers

from . import models


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Event
        exclude = ('deleted_at', 'created_at', 'updated_at')


class GameStartSerializer(serializers.ModelSerializer):
    session_id = serializers.ReadOnlyField()

    class Meta:
        model = models.GameStarted
        exclude = ('deleted_at', 'created_at', 'updated_at')


class GameEndedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GameEnded
        exclude = ('deleted_at', 'created_at', 'updated_at')
