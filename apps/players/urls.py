from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
	url(r'^index/', login_required(views.Index.as_view()), name = 'index'),
    url(r'^create/', login_required(views.Create.as_view()), name = 'create'),
    url(r'^edit/(?P<pk>\w+)/$', login_required(views.Edit.as_view()), name = 'edit'),
    url(r'^delete/(?P<pk>\w+)/$', login_required(views.Delete.as_view()), name = 'delete'),
]