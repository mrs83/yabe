from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from blogs.views import PostList

urlpatterns = patterns('',
    url(r'^$', PostList.as_view(), name='post_list'),
    url(r'^blogs/', include('blogs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.simple.urls')),
)
