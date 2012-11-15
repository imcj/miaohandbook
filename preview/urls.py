from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url ( r'^$', 'preview.views.home', name = 'home' ),
    url ( r'(?P<cat_id>\d+)$', 'preview.views.detail', name = 'detail' ),
    url ( r'(?P<cat_id>\d+)/gallery/$', 'preview.views.gallery', name = 'gallery' )
)
