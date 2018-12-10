from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.views import APIView
from django import views
from judge.tasks import submit
from submission.models import Submission
from users.authentication import NormalUserAuthentication
from users.models import User
from .serializers import SubmissionDeserializer


# Create your views here.
class SubmissionListView(APIView):
    #
    def get(self, request, page=1, *args, **kwargs):
        submissions = Submission.objects.all().order_by('-create_time')
        limit = 20
        paginator = Paginator(submissions, limit)
        submissions = paginator.page(page)
        return render(request, 'submissions/submission_list.html',
                      {'submissions': submissions, 'all': range(1, len(submissions) // limit + 1),
                       'user': request.user})

    # 提交页面
    def post(self, request, *args, **kwargs):
        # print(request.user)
        # print((request.user.is_staff or request.user.is_superuser))
        if not (request.user.is_staff or request.user.is_superuser):
            return render(request, 'submissions/error.html',
                          {
                              'err_message': 'Please login first'
                          })
        ser = SubmissionDeserializer(data=request.data)
        if ser.is_valid():
            instance = ser.save(request.user)
            user = User.objects.get(username=request.user.username)
            user.problem_submit += 1
            user.save()
            submit.delay(instance.id)
            return redirect('submission:submission_list', page=1)
        else:
            return render(request, 'submissions/error.html',
                          {
                              'err_message': 'Please submit all the information, and the min length of code is 50'
                          })


class SubmissionView(APIView):
    # authentication_classes = [NormalUserAuthentication, ]

    def get(self, request, id=1, *args, **kwargs):
        return Response("nihia ")
