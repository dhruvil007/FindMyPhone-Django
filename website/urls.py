from django.conf.urls import url
from website import views

urlpatterns = [
    url(r'^home/$', views.index, name='home'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^locate-phone/$', views.get_location, name='locate-phone'),
    url(r'^make-phone-ring/$', views.make_phone_ring, name='make-phone-ring'),
    url(r'^receive-location/$', views.receive_location, name='receive-location'),
]