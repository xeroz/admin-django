from django.db import models
from apps.teams.models import Team

# Create your models here.
class Player(models.Model):
    name     = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    integer  = models.IntegerField()
    position = models.CharField(max_length=100)
    player   = models.ForeignKey(Team, null=True, blank=True ,on_delete=models.CASCADE)