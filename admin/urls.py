"""admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete

url_password_reset   = {'template_name':'auth/password/send_email.html', 'email_template_name':'auth/password/reset_email.html'}
url_password_done    = {'template':'auth/password/reset_done.html'}
url_password_confirm = {'template_name': 'auth/password/reset_confirm.html'}
url_done = {'template_name': 'registration/password_reset_complete.html'}

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', login, {'template_name':'auth/login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name= 'logout'),
    url(r'^reset/password/$', password_reset, url_password_reset, name='password_reset'),
    url(r'^reset/password_done/$', password_reset_done, url_password_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm, url_password_confirm, name='password_reset_confirm'),
    url(r'^reset/done', password_reset_complete, url_done, name='password_reset_complete'),
    #urls admin
    url(r'^', include('apps.home.urls')),
    url(r'^users/', include('apps.users.urls', namespace='users')),
    url(r'^teams/', include('apps.teams.urls', namespace='teams')),
    url(r'^players/', include('apps.players.urls', namespace='players')),
    url(r'^competitions/', include('apps.competitions.urls', namespace='competitions')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)