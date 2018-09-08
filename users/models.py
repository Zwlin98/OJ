from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True, blank=False, verbose_name='邮箱地址')

    nickname = models.CharField(max_length=50, blank=True, verbose_name='昵称')

    personal_status = models.CharField(max_length=140, blank=True, verbose_name='个性签名')

    problem_solved = models.IntegerField(default=0, verbose_name='通过题目')

    problem_submit = models.IntegerField(default=0, verbose_name='累计提交')

    add_time = models.DateTimeField(default=datetime.now, verbose_name='用户注册时间')

    class Meta(AbstractUser.Meta):
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        pass


class Verifycode(models.Model):
    type_choice = (
        ('active', 'active'),
        ('reset', 'reset')
    )
    code = models.CharField(max_length=50, verbose_name='验证码')
    email = models.EmailField(verbose_name='邮箱')
    send_type = models.CharField(max_length=10,verbose_name='验证码类型', choices=type_choice)
    send_time = models.DateTimeField(verbose_name='生成时间', default=datetime.now)

    class Meta:
        verbose_name = '验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
