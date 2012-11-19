from django.conf.urls import patterns, include, url
from django.contrib import admin
from handbook.api import CatResource, CatPhotoResource, CatFullResource
from tastypie.api import Api
admin.autodiscover()
import settings

v1 = Api ( api_name= 'v1' )
v1.register ( CatResource ( ) )
v1.register ( CatPhotoResource ( ) )
v1.register ( CatFullResource ( ) )
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'miaohandbookweb.views.home', name='home'),
    url(r'^preview/', include('preview.urls')),
    url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to',
    {'url': '/media/img/favicon.ico'}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT, }, name = "media" ),
    url ( r'^api/', include ( v1.urls ) ),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
