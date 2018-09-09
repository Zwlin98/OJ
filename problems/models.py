from datetime import datetime
from django.db import models


# Create your models here.

class Problem(models.Model):
    '''
    基本题目对象
    '''
    i_d = models.CharField(max_length=20, unique=True, verbose_name='题目编号')

    time_limit_C = models.IntegerField(default=1000, verbose_name='时间限制')

    time_limit_other = models.IntegerField(default=2000, verbose_name='其他语言限制')

    memory_limit = models.IntegerField(default=65536, verbose_name='内存限制')

    memory_limit_other = models.IntegerField(default=32768, verbose_name='其他语言内存限制')

    title = models.CharField(max_length=1000, verbose_name='题目标题')

    description = models.TextField(verbose_name='题目描述')

    input_decscription = models.TextField(verbose_name='输入描述')

    output_decscription = models.TextField(verbose_name='输出描述')

    sample_input = models.TextField(verbose_name='样例输入')

    sample_output = models.TextField(verbose_name='样例输出')

    hint = models.TextField(blank=True, verbose_name='题目提示')

    source = models.CharField(max_length=200, blank=True, verbose_name='题目来源')

    add_time = models.DateTimeField(default=datetime.now, verbose_name='题目添加时间')

    accepted = models.IntegerField(default=0, verbose_name='通过人数')

    submitted = models.IntegerField(default=0, verbose_name='提交人数')

    def __str__(self):
        return self._id
