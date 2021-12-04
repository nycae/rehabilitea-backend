from django.utils import timezone
from django.db import models


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def delete(self, **kwargs):
        self.deleted_at = timezone.now()
        self.save()


class Difficulty(Base):
    name = models.CharField(max_length=20, unique=True, null=False)
    games = models.ManyToManyField('Game', blank=True)
    order = models.IntegerField(default=0, null=False)

    class Meta:
        verbose_name_plural = 'difficulties'

    def __str__(self):
        return self.name


class Game(Base):
    name = models.CharField(max_length=50, unique=True, null=False)
    description = models.TextField()
    difficulties = models.ManyToManyField(to=Difficulty, through=Difficulty.games.through, blank=True)

    def __str__(self):
        return self.name
