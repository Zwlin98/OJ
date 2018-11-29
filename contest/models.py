from django.db import models
from datetime import datetime
from problems.models import Problem
# Create your models here.
# from problems.models import Problem

class Contest(models.Model):

    '''
    基本比赛对象
    '''
    contest_id = models.CharField(max_length=20, unique=True, primary_key=True, verbose_name='比赛编号')

    title = models.CharField(max_length=1000, verbose_name='比赛标题', blank=True)

    description = models.TextField(verbose_name='比赛描述', blank=True)

    add_time = models.DateTimeField(default=datetime.now, verbose_name='比赛开始时间')

    people = models.IntegerField(default=0, verbose_name='报名人数')

    source = models.CharField(max_length=200, blank=True, verbose_name='出题人来源')

    # problem_list = models.ForeignKey(Problem)

    def __str__(self):
        return self.id




class  Contest_problem(models.Model):
    '''
    比赛与题目的连接
    '''
    # problem_id = models.CharField(max_length=20,primary_key=True)
    problem_id = models.ForeignKey(Problem)
    contest_id = models.ForeignKey(Contest,primary_key=True)


