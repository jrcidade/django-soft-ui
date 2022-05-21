# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import patient
from .models import user_info


# Register your models here.
admin.site.register(patient)
admin.site.register(user_info)