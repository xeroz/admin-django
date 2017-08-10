from django.contrib import admin
from apps.teams.models import Team, Stadium, PointOfInterest

# Register your models here.
admin.site.register(Team)
admin.site.register(Stadium)
admin.site.register(PointOfInterest)
