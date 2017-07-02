from django.db import models

# Create your models here.
class Team(models.Model):
    name       = models.CharField(max_length=50, default='')
    foundation = models.DateField()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Stadium(models.Model):
    name     = models.CharField(max_length=50, default='')
    image    = models.ImageField(upload_to='stadium_image', blank=True)
    capacity = models.IntegerField(default=10)
    team     = models.OneToOneField(Team)
