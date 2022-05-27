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
    path('updatebilling/<patient.id>/', views.updatebilling, name='updatebilling'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
