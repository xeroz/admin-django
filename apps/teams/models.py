from django.db import models
from django_countries.fields import CountryField
from geoposition.fields import GeopositionField

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=50, default='')
    foundation = models.DateField()
    image = models.ImageField(upload_to='team_image', blank=True)
    country = CountryField(blank_label='select country', null=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Stadium(models.Model):
    name = models.CharField(max_length=50, default='')
    image = models.ImageField(upload_to='stadium_image', blank=True)
    capacity = models.IntegerField(default='')
    team = models.OneToOneField(Team, related_name='team_stadium')
    position = GeopositionField(null=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class PointOfInterest(models.Model):
    name = models.CharField(max_length=100)
    position = GeopositionField()