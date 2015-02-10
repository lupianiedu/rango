# -*- coding: UTF8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
# The settings module from django.conf allows us access to the variables defined within our project’s settings.py file
from django.conf import settings

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'tango_with_django_project.views.home', name='home'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^rango/', include('rango.urls')),
)

# The conditional statement checks if the Django project is being run in DEBUG mode.
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
