from django.db import models

# Create your models here.
class Competition(models.Model):
    name  = models.CharField(max_length=50, default='')
    image = models.ImageField(upload_to='competition_image', blank=True)