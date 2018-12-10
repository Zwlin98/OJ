from django.db import models
from contest.models import Contest
from problems.models import Problem
from users.models import User
from datetime import datetime


# Create your models here.
class JudgeStatus:
    COMPILE_ERROR = 0
    WRONG_ANSWER = 1
    ACCEPTED = 2
    TIME_LIMIT_EXCEEDED = 3
    MEMORY_LIMIT_EXCEEDED = 4
    RUNTIME_ERROR = 5
    SYSTEM_ERROR = 6
    PENDING = 7
    JUDGING = 8
    PARTIALLY_ACCEPTED = 9

    STATUS = [
        'Compile Error',
        'Wrong Answer',
        'Accepted',
        'Time Limit Exceeded',
        'Memory Limit Exceeded',
        'Runtime Error',
        'System Error',
        'Pending',
        'Judging',
        'Partially Accepted'
    ]


class SubmissionLanguage:
    GPP = 0  # G++
    GCC = 1
    CPP = 2
    C = 3
    PASCAL = 4
    JAVA = 5
    CSHARP = 6  # C#

    LANGUAGE = (
        'G++',
        'GCC',
        'C++',
        'C',
        'Pascal',
        'Java',
        'C#'
    )


class Submission(models.Model):
    contest = models.ForeignKey(Contest, null=True, on_delete=models.SET_NULL)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    create_time = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.IntegerField(default=SubmissionLanguage.CPP)
    code = models.TextField()
    result = models.CharField(default=JudgeStatus.STATUS[7], max_length=64)
    exe_time = models.CharField(default='0MS', max_length=64)
    exe_memory = models.CharField(default='0K', max_length=64)
    code_len = models.CharField(default='0B', max_length=64)

    @property
    def get_result(self):
        return JudgeStatus.STATUS[self.result]

    @property
    def get_language(self):
        return SubmissionLanguage.LANGUAGE[self.language]

    def __str__(self):
        return str(self.id)


class HduSubmission(models.Model):
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    hdu_run_id = models.IntegerField()

    def __str__(self):
        return str(self.hdu_run_id)
