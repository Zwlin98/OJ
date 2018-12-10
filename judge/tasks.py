from __future__ import absolute_import, unicode_literals

from celery import shared_task
from judge.models import JudgePlatform
from judge.submitter import HduSubmitter
from submission.models import Submission, HduSubmission
from judge.Spider import HduSpider

@shared_task
def submit(pid):
    instance = Submission.objects.get(id=pid)
    if instance.problem.vjudge == JudgePlatform.HDU:
        submitter = HduSubmitter()
        submitter.login(username='geektest', password='123456')
        submitter.submit(problem=instance.problem, language=instance.language, code=instance.code)
        run_id = submitter.get_run_id(username='geektest')
        if not HduSubmission.objects.filter(hdu_run_id=run_id):
            hdu_submit = HduSubmission()
            hdu_submit.submission = instance
            hdu_submit.hdu_run_id = run_id
            hdu_submit.save()
            return hdu_submit.id
        else:
            return -1

@shared_task
def spider():
    sp = HduSpider(username='geektest')
    return sp.check_database()

