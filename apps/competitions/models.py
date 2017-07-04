from django.db import models
from apps.teams.models import Team

# Create your models here.
class Competition(models.Model):
    name  = models.CharField(max_length=50, default='')
    image = models.ImageField(upload_to='competition_image', blank=True)
    team  = models.ManyToManyField(Team)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name