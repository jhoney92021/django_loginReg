from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index), 
    url(r'^process$', views.process), 
    url(r'^process/registration$', views.processRegistration), 
    url(r'^process/login$', views.processLogin), 
    url(r'^success/$', views.success), 
    url(r'^logout/$', views.logout), 
]