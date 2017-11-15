# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from enum import Enum

class EquipmentType(Enum):
    BIKE = 1


class IntervalType(Enum):
    KMS_RIDING = 1
    HOURS_RIDING = 2
    DAYS = 3
    MONTHS = 4

#the thing that needs fixing sometimes
class Equipment(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField()
    equipment_type = EquipmentType

    def __str__(self):
        return self.name

# sometimes we use the thing
class EquipmentActivity(models.Model):
    name = models.CharField(max_length=200)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    date_of_activity = models.DateTimeField()
    length_km = models.DecimalField
    elapsed_time = models.DurationField
    moving_time = models.DurationField

    def __str__(self):
        return self.name

#what needs fixing on the thing? how often do we want to fix it
class MaintenanceTask(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    interval = models.IntegerField
    interval_type = IntervalType

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
