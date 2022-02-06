from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models

from games.models import Game, Difficulty


class Progression(models.Model):
    user = models.ForeignKey(to=User, db_constraint=False,
                             on_delete=models.DO_NOTHING)
    game = models.ForeignKey(to=Game, db_constraint=False,
                             on_delete=models.DO_NOTHING)
    difficulty = models.ForeignKey(to=Difficulty, db_constraint=False,
                                   on_delete=models.DO_NOTHING)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def delete(self, **kwargs):
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.user.username} has beaten {self.game.name} on " + \
               f"{self.difficulty.name} difficulty"

    class Meta:
        unique_together = ('user', 'game', 'difficulty')
