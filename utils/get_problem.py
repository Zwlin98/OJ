import json
import os
from datetime import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "OJ.settings")
import django
import os

django.setup()

from problems.models import Problem
from contest.models import Contest
from users.models import User

# 这个脚本好像不能应对  models的外键修改
delete_sql = False
if delete_sql:
    if os.path.exists('../db.sqlite3'):
        os.remove('../db.sqlite3')
    result = os.popen('python ../manage.py makemigrations')
    for line in result:
        print(line)
    result = os.popen('python ../manage.py migrate --run-syncdb').readlines()
    for line in result:
        print(line)


user = User()
user.username = 'jj2'
user.set_password("123456")
user.email="df@zwl.com"
user.is_staff = True
user.save()


user = User()
user.username = 'zwlin'
user.set_password("123456")
user.email="zwl@zwl.com"
user.is_staff = True
user.save()


# 插入一个比赛
C = Contest()
C.description = '写脚本真累'
C.participant = 200
C.source = 'zwlin'
C.title = 'Testing_Contest'
C.create_user = User.objects.get(username='zwlin')
C.save()

with open("./item.json", 'r') as f:
    problems = json.load(f)
    id = 1000
    for item in problems:
        p = Problem()
        p.problem_id = str(id)
        p.title = item.get('Title', '')
        p.description = item.get('ProblemDescription', '')
        p.input_description = item.get('Input', '')
        p.output_description = item.get('Output', '')
        p.sample_input = item.get('SampleInput', '')
        p.sample_output = item.get('SampleOutput', '')
        p.hint = item.get('Hint', '')
        p.source = item.get('Author', '')
        # 插入1个题目 , 插入外键需要 两个contest 以及 problem 实例 不好改
        if id <= 1010:
            p.contest = Contest.objects.get(pk=1)
        p.save()
        id += 1
        # str_id = str(id + 2000)
        # CP = Contest_problem()
        # CP.contest_problem_id = str_id
        # CP.contest_id = 'A001'
        # CP.accepted = id
        # CP.submitted = (id) * id / 10
        #
        # CP.problem_id = p.problem_id
        # CP.title = p.title
        # CP.description = p.description
        # CP.input_decscription = p.input_decscription
        # CP.output_decscription = p.output_decscription
        # CP.sample_input = p.sample_input
        # CP.sample_output = p.sample_output
        # CP.hint = p.hint
        # CP.source = CP.source
        # print(CP)
        # CP.save()
