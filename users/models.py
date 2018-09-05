from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    
    nickname = models.CharField(max_length=50, blank=True)

    personal_status = models.CharField(max_length=140, blank=True)

    problem_solved = models.IntegerField(default=0)

    problem_submit = models.IntegerField(default=0)

    class Meta(AbstractUser.Meta):
        pass
