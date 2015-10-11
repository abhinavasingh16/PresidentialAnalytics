from django.conf.urls import patterns, include, url
from analytics_main.views import index
from analytics_main import urls as analytics_main_urls
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pres_analytics_site.views.home', name='home'),
    # url(r'^pres_analytics_site/', include('pres_analytics_site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'/',index,name='home'),
    url(r'',include(analytics_main_urls))
)
