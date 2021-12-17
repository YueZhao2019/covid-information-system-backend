# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.db import models


# Create your models here.

class Covid(models.Model):
    guid = models.CharField(max_length=15,unique=True)
    name = models.CharField(max_length=60,null=True)
    role = models.IntegerField(default=1, null=True)  # 1:Student; 2:Teacher; 3:Administrator
    profile = models.TextField(null=True, blank=True)
    major = models.IntegerField(default=0,null=True) # 1:Software Development; 2:Information Technology; 3:IT Cyber Security
    vaccinated = models.NullBooleanField()
    vaccinated_time = models.DateField(null=True, blank=True)
    infected = models.NullBooleanField()
    recovered = models.NullBooleanField()
    recovered_time = models.DateField(null=True, blank=True)
    apply_result = models.IntegerField(default=0,null=True) # 0:Haven't apply; 1:Approve; 2:Reject; 3:Wait;


    class Meta:
        db_table = "student_covid_information"
