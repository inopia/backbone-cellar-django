from django.conf.urls.defaults import patterns, include, url

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url('^api/wines/$', 'winecellar.api.wines_handler'),
    url('^api/wines/(?P<wine_id>\d+)[/]?$', 'winecellar.api.wines_handler'),
    url('^$', 'winecellar.views.index'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
            url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                'document_root': settings.MEDIA_ROOT,
                }),
            )
    urlpatterns += staticfiles_urlpatterns()
