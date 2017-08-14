from django.conf.urls import url
from apps.players import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^list/', login_required(views.ListPlayer.as_view()), name = 'list'),
    url(r'^create/', login_required(views.CreatePlayer.as_view()), name = 'create'),
    url(r'^edit/(?P<pk>\w+)/$', login_required(views.EditPlayer.as_view()), name = 'edit'),
    url(r'^delete/(?P<pk>\w+)/$', login_required(views.DeletePlayer.as_view()), name = 'delete'),
    url(r'^report_player/(?P<pk>\w+)/$', views.report_player, name = 'report_player'),
    url(r'^test_report/', views.test_report, name = 'test_report'),
]