from django.conf.urls import url
from website import views

urlpatterns = [
    url(r'^home/$', views.index, name='home'),
    url(r'^locate-phone/$', views.get_location, name='locate-phone'),
]