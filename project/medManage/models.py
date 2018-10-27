# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

"""
Basic models.
More advanced versions could have more specialized fields. For example:
Medication - dosage, side effects, manufacturer
Patient - last name, email, address, insurance plan, date added
"""
class Medication(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Patient(models.Model):
    name = models.CharField(max_length=100)
    medications = models.ManyToManyField(Medication, related_name='medications', blank=True)
