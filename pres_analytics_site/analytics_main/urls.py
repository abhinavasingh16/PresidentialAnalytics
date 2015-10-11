from django.conf.urls import patterns, include, url
from analytics_main import views
from analytics_main.views import *

urlpatterns = patterns('',
	url(r"^$",views.index,name="home"),
)
