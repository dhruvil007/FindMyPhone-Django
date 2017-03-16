from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^ring/$', views.make_phone_ring, name='make_phone_ring'),
]