# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from enum import Enum
import os

from datetime import timedelta

#the thing that needs fixing sometimes
class Equipment(models.Model):

    BIKE = "bike"

    EQUIPMENT_TYPE_CHOICES= (
        (BIKE, "Bike"),
    )

    name = models.CharField(max_length=200)
    created_date = models.DateTimeField()
    equipment_type = models.CharField(max_length=2,choices=EQUIPMENT_TYPE_CHOICES,default=BIKE)

    def __str__(self):
        return self.name

# sometimes we use the thing
class EquipmentActivity(models.Model):
    name = models.CharField(max_length=200)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    date_of_activity = models.DateTimeField()
    length_km = models.DecimalField(max_digits=10, decimal_places=2)
    elapsed_time = models.DurationField(default=timedelta(seconds=0))
    moving_time = models.DurationField(default=timedelta(seconds=0))

    def __str__(self):
        return self.name

#what needs fixing on the thing? how often do we want to fix it
class MaintenanceTask(models.Model):

    KM = "km"
    HOURS = "hr"
    DAYS = "d"
    MONTHS = "m"

    INTERVAL_TYPE_CHOICES = (
        (KM, 'km'),
        (HOURS, 'Hours (used)'),
        (DAYS, 'Days (total)'),
        (MONTHS, 'Months (total)'),
    )

    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    interval = models.IntegerField()
    interval_type = models.CharField(max_length=2, choices=INTERVAL_TYPE_CHOICES,default=KM)

    def __str__(self):
        return self.description

    def isRequired(date):
        ''' return if this task is required to be performed at a particular date'''
        return true;

#a record of fixing the thing
class MaintenanceActivity(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    maintenance_tast = models.ForeignKey(MaintenanceTask, on_delete=models.CASCADE)
    date_of_maintenance = models.DateTimeField()
