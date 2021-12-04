from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models

from games.models import Game


class Base(models.Model):
    game = models.ForeignKey(to=Game, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True


class Event(Base):
    description = models.CharField(max_length=50, null=False)

    def delete(self, **kwargs):
        self.deleted_at = timezone.now()
        self.save()


class GameStarted(Base):
    session_id = models.AutoField(primary_key=True)


class GameEnded(Base):
    session_id = models.IntegerField(null=False)

    score = models.IntegerField()
    max_score = models.IntegerField()
