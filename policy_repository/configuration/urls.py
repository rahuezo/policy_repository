from django.conf.urls import url

from . import views

app_name = 'configuration'

urlpatterns = [
    url(r'^$', views.configuration_view, name='configuration'),
    url(r'^update_people/$', views.update_people_view, name='update_people'),
    url(r'^upload_files/$', views.upload_files_to_library_view, name='upload_files'),
    url(r'^add_policy_subtype/$', views.add_policy_subtype_view, name='add_policy_subtype'),
    url(r'^add_municipality_type/$', views.add_muni_type_view, name='add_municipality_type'),

]
