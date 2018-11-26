from django.http import Http404
from django.shortcuts import render

from django.views.generic.base import View
from contest.models import Contest

from django.core.paginator import Paginator

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
    def get(self,request,id):
        try:
            contest = Contest.objects.get(id=id)
            return render(request, 'contest/contest.html', {'contest': contest})
        except Exception:
            raise Http404