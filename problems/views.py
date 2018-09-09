from django.shortcuts import render
from django.http import Http404
from django.views.generic.base import View
from django.core.paginator import Paginator
from .models import Problem
# Create your views here.

from .models import Problem


class ProblemListView(View):
    def get(self, request, page=1):
        problems = Problem.objects.all()
        limit = 20
        paginator = Paginator(problems, limit)
        problem_list = paginator.page(page)
        return render(request, 'problems/problems_list.html', {'problem_list': problem_list})


def get_problem(request, id):
    try:
        problem = Problem.objects.get(i_d=id)
        return render(request, 'problems/problem.html', {'problem': problem})
    except Exception:
        raise Http404
