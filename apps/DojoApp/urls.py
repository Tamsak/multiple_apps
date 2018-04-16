from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
 url(r'^$', views.index, name='Blogs'),   # This line has changed!
 url(r'^new$', views.new, name ='New'),
 url(r'^create$', views.create),
 url(r'^(?P<blog>\d+)$', views.show),
 url(r'^(?P<blog>\d+)/edit/$', views.edit),
 url(r'^(?P<blog>\d+)/destroy/$', views.destroy),
]