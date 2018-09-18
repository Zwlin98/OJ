import json

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "OJ.settings")
import django
django.setup()

from problems.models import Problem
with open("./item.json", 'r') as f:
    problems = json.load(f)
    id=1000
    for item in problems:
        p = Problem()
        p.id = str(id)
        id+=1
        p.title = item.get('Title','')
        p.description = item.get('ProblemDescription','')
        p.input_decscription = item.get('Input','')
        p.output_decscription = item.get('Output','')
        p.sample_input = item.get('SampleInput','')
        p.sample_output = item.get('SampleOutput','')
        p.hint =item.get('Hint','')
        p.source = item.get('Author','')
        p.save()


