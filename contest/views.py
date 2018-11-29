from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic.base import View
from django.forms.models import model_to_dict

from contest.models import Contest, Contest_problem
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
        # contest_problem = Contest_problem.objects.get(contest_problem_id=id)

        contest = Contest.objects.filter(contest_id=id)
        contest_problem_list = Contest_problem.objects.filter(contest_id=id)
        test = contest_problem_list.values('problem_id')
        # problem_list = Problem.objects.filter(problem_id__in=['1000','1001','1002'])
        problem_list = Problem.objects.filter(problem_id__in=contest_problem_list.values('problem_id'))
        # problem_list = Problem.objects.filter(problem_id=test[0].values('problem_id'))

        # problem_list = []
        # for tmp in contest_problem:
        #     problem_list.append(Problem.objects.filter(problem_id__in=)))

        # 加入题目信息
        # qy_problem = Contest_problem.objects.filter(contest_id=id).values('problem_id')
        # problem_list = Problem.objects.filter(problem_id=qy_problem).all()
        # contest = {}
        # context['contest'] = contest
        # context['problem_list'] = problem_list
        # context['contest_problem)lis']
        problem_list = [problem for problem in problem_list]
        contest_problem_list  = [ cp for cp  in contest_problem_list]
        # 仍是一个查询
        # contest_problem_list = contest_problem_list.values()
        return render(request, 'contest/contest.html',
                      {
                          'contest': contest[0],
                          'problem_list': problem_list,
                          'contest_problem_list': contest_problem_list
                      }
                      )
        # except Exception:
        #     raise Http404
