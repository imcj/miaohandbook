from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'miaohandbookweb.views.home', name='home'),
    url(r'^preview/', include('preview.urls')),
    url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to',
    {'url': '/media/img/favicon.ico'}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT, }, name = "media" ),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
