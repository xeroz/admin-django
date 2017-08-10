from django.db import models
from apps.teams.models import Team
from django_countries.fields import CountryField

# Create your models here.


class Player(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    number = models.IntegerField()
    position = models.CharField(max_length=100)
    team = models.ForeignKey(
        Team,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='player_image', blank=True)
    country = CountryField(blank_label='select country', null=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Statistics(models.Model):
    pace = models.IntegerField()
    shooting = models.IntegerField()
    passing = models.IntegerField()
    dribbling = models.IntegerField()
    defending = models.IntegerField()
    physical = models.IntegerField()
    player = models.OneToOneField(Player, related_name='statistic')
