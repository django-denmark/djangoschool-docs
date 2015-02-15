from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.post_list, name='post_wall'),
    url(r'^post/new/$', views.post_write_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
)
