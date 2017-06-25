from django.db import models
from apps.teams.models import Team

# Create your models here.
class Player(models.Model):
    name     = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    number   = models.IntegerField()
    position = models.CharField(max_length=100)
    team     = models.ForeignKey(Team, null=True, blank=True ,on_delete=models.CASCADE)