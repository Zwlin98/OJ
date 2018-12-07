from datetime import datetime, timedelta

from django.db import models

from users.models import User

from django.contrib.postgres.fields import JSONField


# Create your models here.
# from problems.models import Problem
class ContestType:
    ACM = 1
    OI = 2
    Other = 3


class ContestStatus:
    CONTEST_NOT_START = 1
    CONTEST_ENDED = 2
    CONTEST_UNDERWAY = 3


def get_end_time():
    return datetime.now() + timedelta(hours=5)


class Contest(models.Model):
    '''
    基本比赛对象
    '''

    title = models.CharField(max_length=1000, verbose_name='比赛标题', blank=True)

    description = models.TextField(verbose_name='比赛描述', blank=True)

    start_time = models.DateTimeField(default=datetime.now, verbose_name='比赛开始时间')

    end_time = models.DateTimeField(default=get_end_time)

    type = models.IntegerField(default=ContestType.ACM, verbose_name="Contest type")

    participant = models.IntegerField(default=0, verbose_name='报名人数')

    source = models.CharField(max_length=200, blank=True, verbose_name='出题人来源')

    create_user = models.ForeignKey(User, on_delete=models.CASCADE)

    create_time = models.DateTimeField(auto_now_add=True)

    visible = models.BooleanField(default=True)

    @property
    def status(self):
        if self.start_time > datetime.now():
            return ContestStatus.CONTEST_NOT_START
        elif self.end_time < datetime.now():
            return ContestStatus.CONTEST_ENDED
        else:
            return ContestStatus.CONTEST_UNDERWAY

    def __str__(self):
        return self.id  # 增加代码


class AbstractContestRank(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    submission_number = models.IntegerField(default=0)

    class Meta:
        abstract = True


class ACMContestRank(AbstractContestRank):
    accepted_number = models.IntegerField(default=0)
    # total_time is only for ACM contest, total_time =  ac time + none-ac times * 20 * 60
    total_time = models.IntegerField(default=0)
    # {"23": {"is_ac": True, "ac_time": 8999, "error_number": 2, "is_first_ac": True}}
    # key is problem id
    submission_info = JSONField(default=dict)


class OIContestRank(AbstractContestRank):
    total_score = models.IntegerField(default=0)
    # {"23": 333}
    # key is problem id, value is current score
    submission_info = JSONField(default=dict)


class ContestAnnouncement(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    title = models.TextField()
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    visible = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-create_time",)

# class Contest_problem(models.Model):
#     '''
#     比赛与题目的连接
#     '''
#
#     # contest_problem_id = models.CharField(max_length=5,primary_key=True)
#
#     # 能不能用外键？ 我试了半天有点蒙
#     # problem= models.ForeignKey(Problem,on_delete=models.DO_NOTHING,related_name='problem')
#     # problem_id = models.CharField(max_length=20,default='1000')
#     problem_id = models.CharField(max_length=20, unique=True, primary_key=True, verbose_name='题目编号')
#
#     contest_id = models.CharField(max_length=20, default='A001')
#
#     contest_problem_id = models.CharField(max_length=20, default='NULL')
#
#     time_limit_C = models.IntegerField(default=1000, verbose_name='时间限制')
#
#     time_limit_other = models.IntegerField(default=2000, verbose_name='其他语言限制')
#
#     memory_limit = models.IntegerField(default=65536, verbose_name='内存限制')
#
#     memory_limit_other = models.IntegerField(default=32768, verbose_name='其他语言内存限制')
#
#     title = models.CharField(max_length=1000, verbose_name='题目标题', blank=True)
#
#     description = models.TextField(verbose_name='题目描述', blank=True)
#
#     input_decscription = models.TextField(verbose_name='输入描述', blank=True)
#
#     output_decscription = models.TextField(verbose_name='输出描述', blank=True)
#
#     sample_input = models.TextField(verbose_name='样例输入', blank=True)
#
#     sample_output = models.TextField(verbose_name='样例输出', blank=True)
#
#     hint = models.TextField(blank=True, verbose_name='题目提示')
#
#     source = models.CharField(max_length=200, blank=True, verbose_name='题目来源')
#
#     add_time = models.DateTimeField(default=datetime.now, verbose_name='题目添加时间')
#
#     accepted = models.IntegerField(default=0, verbose_name='通过人数')
#
#     submitted = models.IntegerField(default=0, verbose_name='提交人数')
#
#     def __str__(self):
#         return self.problem_id  # 增加代码
