"""pool_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from games import views as game_views
from . import views as home_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^players/new/$', game_views.create_player),
    url(r'^players/$', game_views.players),
    url(r'^games/new/$', game_views.create_game),
    url(r'^games/$', game_views.games),
    url(r'^$', home_views.home)
    
] + staticfiles_urlpatterns()