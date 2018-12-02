import json
import os
from  datetime import datetime
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "OJ.settings")
import django
import os

django.setup()

from problems.models import Problem
from contest.models import Contest, Contest_problem


# 这个脚本好像不能应对  models的外键修改
if os.path.exists('db.sqlite3'):
    os.remove('db.sqlite3')


result = os.popen('python manage.py makemigrations')
for line in result:
    print(line)
result = os.popen('python manage.py migrate --run-syncdb').readlines()
for line in result:
    print(line)




# 插入一个比赛
C = Contest()

C.contest_id = 'A001'
date = datetime.now
# 这个东西没法直接插入，？ 怎么写
# C.add_time = date
C.description = '写脚本真累'
C.people = 200
C.source = '胡一一'
C.title = '这一个自动AC的Contest'
C.save()



with open("./item.json", 'r') as f:
    problems = json.load(f)
    id = 1000
    for item in problems:
        p = Problem()
        p.problem_id = str(id)
        id += 1
        p.title = item.get('Title', '')
        p.description = item.get('ProblemDescription', '')
        p.input_decscription = item.get('Input', '')
        p.output_decscription = item.get('Output', '')
        p.sample_input = item.get('SampleInput', '')
        p.sample_output = item.get('SampleOutput', '')
        p.hint = item.get('Hint', '')
        p.source = item.get('Author', '')

        # 加入比赛的题目可选选择性的不可视，这里选择都不可视
        if id <= 1010:
            p.is_visual = False
            p.is_contested = True
        p.save()

    # 插入1个题目 , 插入外键需要 两个contest 以及 problem 实例 不好改
    for i in range(0, 10):
        id = str(i + 2000)
        CP = Contest_problem()
        CP.contest_problem_id = id
        CP.problem_id = str(i+1000)
        CP.contest_id = 'A001'
        CP.accepted_num = 0
        CP.submit_num = 50* i
        CP.title = '表打我，我是'+id+'啊'
        CP.save()

