from django.shortcuts import render
from django.http import Http404
from django.views.generic.base import View
from django.core.paginator import Paginator

from .models import Problem


# Create your views here.







class ProblemListView(View):
    def get(self, request, page=1):
        problems = Problem.objects.filter(is_visual=True)
        limit = 20
        paginator = Paginator(problems, limit)
        problem_list = paginator.page(page)
        return render(request, 'problems/problems_list.html',
                      {'problem_list': problem_list, 'all': range(1, problems.count() // limit + 1)})


# TODO:编写题目详情
class ProblemView(View):
    def get(self, request, problemid):
        try:
            problem = Problem.objects.get(problem_id=problemid)
            # 因题目正在比赛或其他原因,不可视
            if problem.is_visual == False:
                raise  Http404
            return render(request, 'problems/problem.html', {'problem': problem})
        except Exception:
            raise Http404

    # TODO:Complete  submit problem
    def post(self, request, problemid):
        pass


# TODO:搜索题目逻辑
class SearchProblemView(View):
    pass


def get_problem(request, id):
    pass
