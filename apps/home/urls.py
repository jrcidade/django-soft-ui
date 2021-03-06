# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='index'),
    path('billing', views.billing, name='billing'),
    path('update_patient/<patient_id>', views.update_patient, name='update-patient'),


    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
