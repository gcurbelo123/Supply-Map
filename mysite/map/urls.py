from django.conf.urls import url
from map.views import *
from .import views

urlpatterns = [
   url(r'^$', landing, name="landing"),
   url(r'^home$', landing, name="home"),
   url(r'^disp$', mapping, name="map"),
   url(r'^map$', makeMap, name="map"),
   url(r'^staticmap$', staticMap, name ="staticmap"),
   url(r'^savePic$', save, name= "savePic")
   
]