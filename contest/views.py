from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render
from django.views.generic.base import View
from django.forms.models import model_to_dict

from contest.models import Contest
from problems.models import Problem


# Create your views here.


class ContestListView(View):

    def get(self, request, page=1):
        contests = Contest.objects.all()
        limit = 20
        paginator = Paginator(contests, limit)
        contest_list = paginator.page(page)
        return render(request, 'contest/contest_list.html',
                      {'contest_list': contest_list, 'all': range(1, contests.count() // limit + 1)})


class ContestView(View):
    def get(self, request, id):
        # try:
        # print(id)
        contest = Contest.objects.get(id=id)
        contest_problem_list = Problem.objects.filter(contest=id)
        contest_problem_list = [cp for cp in contest_problem_list]
        return render(request, 'contest/contest.html',
                      {
                          'contest': contest,
                          'contest_problem_list': contest_problem_list
                      }
                      )
        # except Exception:
        #     raise Http404


class ProblemView(View):

    def get(self, request, id):
        try:
            problem = Problem.objects.get(problem_id=id)
            # 因题目正在比赛或其他原因,不可视
            return render(request, 'contest/problem.html',
                          {'contest_problem_list': problem})
        except Exception:
            raise Http404
