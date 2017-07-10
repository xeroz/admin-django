from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^index/', login_required(views.IndexView.as_view()), name = 'index'),
    url(r'^create/', login_required(views.CreateView.as_view()), name = 'create'),
    # url(r'^edit/(?P<id>\w+)/$', login_required(views.edit), name = 'edit'),
    url(r'^edit/(?P<pk>\d+)/$', login_required(views.EditView.as_view()), name = 'edit'),
    url(r'^delete/(?P<pk>\w+)/$', login_required(views.DeleteView.as_view()), name = 'delete'),
    url(r'^players/(?P<id>\w+)/$', login_required(views.players), name = 'players'),
    url(r'^stadium/(?P<id>\w+)/$', login_required(views.stadium), name = 'stadium'),
]