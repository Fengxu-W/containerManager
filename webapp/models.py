# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class User(models.Model):
    account = models.CharField(max_length=30)
    passwd = models.CharField(max_length=30)


class Container(models.Model):
    number = models.CharField(verbose_name='箱号', max_length=30, unique=True)
    type = models.CharField(verbose_name='箱型', max_length=30, null=True, blank=True, default='40HQ')
    usage = models.CharField(verbose_name='使用次数', max_length=10, null=True, blank=True, default=0)
    reference = models.CharField(verbose_name='reference', max_length=30, null=True, blank=True)
    enterDate = models.DateField(verbose_name='进场日', null=True, blank=True)
    roll_outDate = models.DateField(verbose_name='转出堆场日', null=True, blank=True)
    damageCondition = models.CharField(verbose_name='损坏情况', max_length=30, null=True, blank=True, default='良好')

