# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class patient(models.Model):
    Firstname = models.CharField(max_length = 50)
    Lastname = models.CharField(max_length = 100)
    Age = models.IntegerField()
    Date = models.DateTimeField()


    def __str__(self):
        return self.Firstname+' '+self.Lastname

class user_info(models.Model):
    user_name = models.CharField('User name', max_length=128)
    email = models.EmailField('email')

    def __str__(self):
       return self.user_name