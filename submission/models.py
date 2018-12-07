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
    MEMORY_LIMIT_EXCEEDED = 5
    RUNTIME_ERROR = 6
    SYSTEM_ERROR = 7
    PENDING = 8
    JUDGING = 9
    PARTIALLY_ACCEPTED = 10

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
    C = 0
    CPP = 1
    JAVA = 2
    Python = 3

    LANGUAGE = (
        'C',
        'C++',
        'Java',
        'Python'
    )


class Submission(models.Model):

    contest = models.ForeignKey(Contest, null=True, on_delete=models.SET_NULL)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    create_time = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.IntegerField(default=SubmissionLanguage.CPP)
    code = models.TextField()
    result = models.IntegerField(default=JudgeStatus.PENDING)

    @property
    def get_result(self):
        return JudgeStatus.STATUS[self.result]

    @property
    def get_language(self):
        return SubmissionLanguage.LANGUAGE[self.language]

    def __str__(self):
        return self.id
