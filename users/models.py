# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser
from covid.models import Covid


# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=15, unique=True) # username is same as guid
    password = models.CharField(max_length=60, null=True)
    role = models.IntegerField(default=1, null=True)  # 1:student; 2:teacher; 3:administrator
    covid_info = models.OneToOneField(to=Covid,to_field='guid',null=True)

    USERNAME_FIELD= 'username'

    class Meta:
        db_table = "user"


