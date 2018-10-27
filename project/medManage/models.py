# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

#TODO: add other medication info
class Medication(models.Model):
    name = models.CharField(max_length=100, unique=True)

#TODO: add first, last name, email, dateAdded
class Patient(models.Model):
    name = models.CharField(max_length=100)
    medications = models.ManyToManyField(Medication, related_name='medications', blank=True)
