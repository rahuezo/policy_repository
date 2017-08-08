from django.conf.urls import url

from . import views

app_name = 'configuration'

urlpatterns = [
    url(r'^$', views.configuration_view, name='configuration'),
    url(r'^update_people/$', views.update_people_view, name='update_people'),

]