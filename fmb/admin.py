# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

admin.site.register(Equipment)
admin.site.register(EquipmentActivity)
admin.site.register(MaintenanceTask)
admin.site.register(MaintenanceActivity)
