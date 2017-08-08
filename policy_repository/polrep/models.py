# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Policy(models.Model):
    file_path = models.CharField(max_length=1024)
    # word_count = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.file_path

    def __unicode__(self):
        return self.file_path


class Subtype(models.Model):
    subtype_name = models.CharField(max_length=250)

    def __str__(self):
        return self.subtype_name

    def __unicode__(self):
        return self.subtype_name


class Year(models.Model):
    year = models.CharField(max_length=4)

    def __str__(self):
        return self.year

    def __unicode__(self):
        return self.year


class MunicipalityName(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class MunicipalityType(models.Model):
    mtype = models.CharField(max_length=50)

    def __str__(self):
        return self.mtype

    def __unicode__(self):
        return self.mtype


class PolicyStance(models.Model):
    stance = models.CharField(max_length=10)

    def __str__(self):
        return self.stance

    def __unicode__(self):
        return self.stance
