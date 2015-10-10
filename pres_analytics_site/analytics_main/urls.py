from django.conf.urls import patterns, include, url
from analytics_main import views
from analytics_main.views import *

urlpatterns = patterns('',
	url(r"f/",views.index,name="home"),
	url(r"^visualize*",views.visualizer,name="viz"),
)
