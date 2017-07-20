# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Subtype, Year, MunicipalityName, MunicipalityType, PolicyStance, Policy
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(Subtype)
admin.site.register(Year)
admin.site.register(MunicipalityName)
admin.site.register(MunicipalityType)
admin.site.register(PolicyStance)
admin.site.register(Policy)
