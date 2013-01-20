from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

import appviews

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jsonip.views.home', name='home'),
    # url(r'^jsonip/', include('jsonip.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', appviews.homepage, name='homepage'),
    url(r'^about/$', appviews.about, name='about'),
)

handler404 = 'jsonip.appviews.error404'
handler500 = 'jsonip.appviews.error500'
handler403 = 'jsonip.appviews.error403'
