from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^index/', login_required(views.index), name = 'index'),
    url(r'^create/', login_required(views.create), name = 'create'),
]