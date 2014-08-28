from django.conf.urls import patterns, include, url

from blogs import views

urlpatterns = patterns('',
    url(r'^create/$', views.PostCreate.as_view(), name='post_create'),
    url(r'^update/(?P<pk>\d+)/$', views.PostUpdate.as_view(), name='post_update'),
    url(r'^delete/(?P<pk>\d+)/$', views.PostDelete.as_view(), name='post_delete'),
)
