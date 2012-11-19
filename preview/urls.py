from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url ( r'^index.html$', 'preview.views.home', name = 'home' ),
    url ( r'^detail.html$', 'preview.views.detail', name = 'detail' ),
)
