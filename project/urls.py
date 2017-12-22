from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from welcome.views import index, health, openNg2Project, openMusicApp

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index),
    url(r'^health$', health),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ng2/', openNg2Project),
    url(r'^cc-client/', openMusicApp),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
