from django.conf.urls import url, include
from django.contrib import admin

from accounts.views import (login_view, register_view, logout_view)
# from configuration.views import (configuration_view, update_people_view)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', login_view, name='login'),
    url(r'^logout/', logout_view, name='logout'),
    url(r'^register/', register_view, name='register'),
    url(r'^configuration/', include('configuration.urls')),
    # url(r'^configuration/update_people', update_people_view, name='update_people'),

    url(r'^', include('polrep.urls')),
]
