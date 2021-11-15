from django.contrib import admin

from . import models


admin.site.register(models.GameStarted)
admin.site.register(models.GameEnded)
