from datetime import datetime, timedelta

from django.db import models

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

    starttime = models.DateTimeField(default=datetime.now(), verbose_name='比赛开始时间')

    endtime = models.DateField(default=datetime.now()+ timedelta(hours=5),verbose_name='结束时间')

    people = models.IntegerField(default=0, verbose_name='报名人数')

    source = models.CharField(max_length=200, blank=True, verbose_name='出题人来源')


    # problem_list = models.ForeignKey(Problem)

    def __str__(self):
        return self.contest_id   # 增加代码


class Contest_problem(models.Model):
    '''
    比赛与题目的连接
    '''

    # contest_problem_id = models.CharField(max_length=5,primary_key=True)

    # 能不能用外键？ 我试了半天有点蒙
    #problem= models.ForeignKey(Problem,on_delete=models.DO_NOTHING,related_name='problem')
    # problem_id = models.CharField(max_length=20,default='1000')
    problem_id = models.CharField(max_length=20, unique=True, primary_key=True, verbose_name='题目编号')

    contest_id = models.CharField(max_length=20,default='A001')

    contest_problem_id = models.CharField(max_length=20,default='NULL')

    time_limit_C = models.IntegerField(default=1000, verbose_name='时间限制')

    time_limit_other = models.IntegerField(default=2000, verbose_name='其他语言限制')

    memory_limit = models.IntegerField(default=65536, verbose_name='内存限制')

    memory_limit_other = models.IntegerField(default=32768, verbose_name='其他语言内存限制')

    title = models.CharField(max_length=1000, verbose_name='题目标题',blank=True)

    description = models.TextField(verbose_name='题目描述',blank=True)

    input_decscription = models.TextField(verbose_name='输入描述',blank=True)

    output_decscription = models.TextField(verbose_name='输出描述',blank=True)

    sample_input = models.TextField(verbose_name='样例输入',blank=True)

    sample_output = models.TextField(verbose_name='样例输出',blank=True)

    hint = models.TextField(blank=True, verbose_name='题目提示')

    source = models.CharField(max_length=200, blank=True, verbose_name='题目来源')

    add_time = models.DateTimeField(default=datetime.now, verbose_name='题目添加时间')

    accepted = models.IntegerField(default=0, verbose_name='通过人数')

    submitted = models.IntegerField(default=0, verbose_name='提交人数')



    def __str__(self):
        return self.problem_id  # 增加代码
