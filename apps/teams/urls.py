from django.conf.urls import url
from apps.teams import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^list/', login_required(views.ListTeams.as_view()), name = 'list'),
    url(r'^create/', login_required(views.CreateTeam.as_view()), name = 'create'),
    url(r'^edit/(?P<pk>\w+)/$', login_required(views.EditTeam.as_view()), name = 'edit'),
    url(r'^delete/(?P<pk>\w+)/$', login_required(views.DeleteTeam.as_view()), name = 'delete'),
    url(r'^players/(?P<pk>\w+)/$', login_required(views.ListPlayersByTeam.as_view()), name = 'players'),
    url(r'^stadium/(?P<pk>\w+)/$', login_required(views.ListStadiumByTeam.as_view()), name = 'stadium'),
    url(r'^get_players_by_country/$', views.get_players_by_country, name = 'get_players_by_country'),
    url(r'^get_detail_player/$', views.get_detail_player, name = 'get_detail_player'),
]