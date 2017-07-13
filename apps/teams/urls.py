from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^index/', login_required(views.IndexView.as_view()), name = 'index'),
    url(r'^create/', login_required(views.CreateView.as_view()), name = 'create'),
    url(r'^edit/(?P<pk>\d+)/$', login_required(views.EditView.as_view()), name = 'edit'),
    url(r'^delete/(?P<pk>\w+)/$', login_required(views.DeleteView.as_view()), name = 'delete'),
    url(r'^players/(?P<pk>\w+)/$', login_required(views.Players.as_view()), name = 'players'),
    url(r'^stadium/(?P<pk>\w+)/$', login_required(views.Stadiu.as_view()), name = 'stadium'),
    url(r'^json/$', views.fbview, name = 'json'),
    url(r'^get_players_by_country/$', views.get_players_by_country, name = 'get_players_by_country'),
]