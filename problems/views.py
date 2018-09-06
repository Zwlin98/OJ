from django.shortcuts import render
from django.http import Http404
from .models import Problem
# Create your views here.

def get_problem(request,id):
    try:
        problem = Problem.objects.get(idd__exact=id)
        return render(request,'problems/problem.html',{'problem':problem})
    except Exception:
        raise Http404