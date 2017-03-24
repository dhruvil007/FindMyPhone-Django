from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^receive-location/$', views.receive_location, name='receive-location'),
]