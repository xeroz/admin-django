from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^index/', login_required(views.index), name = 'index'),
    url(r'^create/', login_required(views.create), name = 'create'),
    url(r'^edit/(?P<id>\w+)/$', login_required(views.edit), name = 'edit'),
    url(r'^delete/(?P<id>\w+)/$', login_required(views.delete), name = 'delete'),
    url(r'^players/(?P<id>\w+)/$', login_required(views.players), name = 'players'),
    url(r'^stadium/(?P<id>\w+)/$', login_required(views.stadium), name = 'stadium'),
]