from django.db import models

# Create your models here.

class problem(models.Model):
    '''
    基本题目对象
    '''
    problem_id = models.IntegerField(primary_key=True)
    time_limit_C = models.IntegerField(default=1000)
    time_limit_other = models.IntegerField(default=2000)
    memory_limit=models.IntegerField(default=65536)
    problem_description = models.TextField()
    problem_input_decscription = models.TextField()
    problem_output_decscription = models.TextField()
    problem_sample_input = models.TextField()
    problem_sample_output = models.TextField()
    problem_source = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.problem_id