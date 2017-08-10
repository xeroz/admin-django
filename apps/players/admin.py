from django.contrib import admin
from apps.players.models import Player, Statistics

# Register your models here.
admin.site.register(Player)
admin.site.register(Statistics)
