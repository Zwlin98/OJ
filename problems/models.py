from datetime import datetime
from django.db import models


# Create your models here.
#TODO:添加verbose_name
class Problem(models.Model):
    '''
    基本题目对象
    '''
    id = models.CharField(max_length=20,unique=True)
    time_limit_C = models.IntegerField(default=1000)
    time_limit_other = models.IntegerField(default=2000)
    memory_limit = models.IntegerField(default=65536)
    memory_limit_other = models.IntegerField(default=32768)
    description = models.TextField()
    input_decscription = models.TextField()
    output_decscription = models.TextField()
    sample_input = models.TextField()
    sample_output = models.TextField()
    hint = models.TextField(blank=True)
    source = models.CharField(max_length=200, blank=True)
    add_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.problem_id
