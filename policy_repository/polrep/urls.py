from django.conf.urls import url

from . import views
from django.contrib.auth import views as auth_views

app_name = 'polrep'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.retrieve, name='retrieve'),
    url(r'^register/$', views.register, name='register'),
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^signout/$', views.successful_logout, name='successful_logout'),
    url(r'^register_success/$', views.register_success, name='register_success'),
    url(r'^pdf_viewer/(?P<pdf_name>[-\w.]+)$', views.pdf_viewer, name='pdf_viewer'),
    url(r'^pdf_download/(?P<pdf_name>[-\w.]+)$', views.pdf_download, name='pdf_download'),
]
