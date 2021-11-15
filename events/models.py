from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models

from games.models import Game


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True)

    def delete(self, **kwargs):
        self.deleted_at = timezone.now()
        self.save()


class GameStarted(Base):
    game = models.ForeignKey(to=Game, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)


class GameEnded(Base):
    game = models.ForeignKey(to=Game, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)

    score = models.IntegerField()
    max_score = models.IntegerField()
