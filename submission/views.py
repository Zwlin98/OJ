from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.views import APIView
from django import views
from judge.tasks import submit
from submission.models import Submission
from users.authentication import NormalUserAuthentication
from .serializers import SubmissionDeserializer


# Create your views here.
class SubmissionListView(APIView):
    #
    def get(self, request, page=1, *args, **kwargs):
        submissions = Submission.objects.all().order_by('-create_time')
        limit = 20
        paginator = Paginator(submissions, limit)
        submissions = paginator.page(page)
        return render(request,'submissions/submission_list.html',
                      {'submissions': submissions, 'all': range(1, len(submissions)// limit + 1),
                       'user': request.user})


    # 提交页面
    def post(self, request, *args, **kwargs):
        # print(request.user)
        # print((request.user.is_staff or request.user.is_superuser))
        if not (request.user.is_staff or request.user.is_superuser):
            return Response("Please login first")
        ser = SubmissionDeserializer(data=request.data)
        if ser.is_valid():
            instance = ser.save(request.user)
            submit.delay(instance.id)
            return HttpResponseRedirect(reverse('submission:submission_list'))  # 跳转到index界面
        else:
            return HttpResponseRedirect(reverse('problems:problem_list submission_list'))  # 跳转到index界面
            #
            # return render('problems.html',
            #               {'msg': ser.errors, 'errors': True})


class SubmissionView(APIView):
    # authentication_classes = [NormalUserAuthentication, ]

    def get(self,request,id=1,*args,**kwargs):
        return Response("nihia ")