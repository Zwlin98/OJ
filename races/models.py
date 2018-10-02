import datetime
from django.db import models
from django import forms

# Create your models here.
from django.db.models import CharField, DateTimeField, IntegerField


class race(models.Model):
    race_name = CharField(unique=True, blank=False, verbose_name='比赛名称')
    add_time = DateTimeField(default=datetime.now, verbose_name='用户注册时间')
    
    class Meta:
        #什么意思？？？
        verbose_name = '？？？？'
        verbose_name_plural = verbose_name

class race_problems_list(forms):
    problems_listlist = IntegerField(unique=True, blank=False, verbose_name='题目编号');
