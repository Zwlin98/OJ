from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from contest.models import Contest
from judge.tasks import submit
from problems.models import Problem
from users.models import User
from .serializers import SubmissionDeserializer
from submission.models import SubmissionLanguage, Submission


# Create your views here.
class SubmissionListView(APIView):
    #
    def get(self, request, page=1, *args, **kwargs):
        # submissions 对象list
        submissions = Submission.objects.all().order_by('-create_time')
        limit = 20
        paginator = Paginator(submissions, limit)
        submissions = paginator.page(page)

        return render(request, 'submissions/submission_list.html',
                      {'submissions': submissions, 'all': range(1, len(submissions) // limit + 1),
                       'language': SubmissionLanguage.LANGUAGE,
                       # 'submissions_lange'
                       'user_id': request.user.id,

                       })

    # 提交页面
    def post(self, request, *args, **kwargs):
        # print(request.user)
        # print((request.user.is_staff or request.user.is_superuser))
        if not request.user.is_active:
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
    def get(self, request, submission_id, *args, **kwargs):
        try:
            submission = Submission.objects.get(id=submission_id)
        except:
            return render(request, 'submissions/error.html',
                          {
                              'err_message': '404 Not Found'
                          })
        # 需要细粒度更高的认证
        if request.user.id != submission.user.id:
            return render(request, 'submissions/error.html',
                          {
                              'err_message': '这不是你的代码,无权查看.'
                          })

        problem = Problem.objects.get(problem_id=submission.problem.problem_id)
        try:
            contest = Contest.objects.get(id=submission.contes.id)
        except Exception as e:
            contest = None
        # print(problem)
        return render(request, "submissions/submission.html",
                      {
                          'submission': submission,
                          'problem': problem,
                          'contest': contest,
                          # 'language':SubmissionLanguage.LANGUAGE
                          'language': SubmissionLanguage.LANGUAGE,
                      }
                      )
