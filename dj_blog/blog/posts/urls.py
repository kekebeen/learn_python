from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^create/$', views.post_create),
    url(r'^details/(?P<id>\d+)', views.post_detail, name="details"),
    url(r'^$', views.post_list, name="index"),
    url(r'(?P<id>\d+)/edit/$', views.post_update, name="update"),
    url(r'^delete/$', views.post_delete)
]