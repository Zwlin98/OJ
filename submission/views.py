from django.core.paginator import Paginator
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from submission.models import Submission
from .serializers import SubmissionSerializer, SubmissionDeserializer
from users.authentication import NormalUserAuthentication
from judge.tasks import submit


# Create your views here.
class SubmissionListView(APIView):
    #
    def get(self, request, page=1, *args, **kwargs):
        submissions = Submission.objects.all()
        limit = 20
        paginator = Paginator(submissions, limit)
        submissions = paginator.page(page)
        self.dispatch()
        return render('submission_list.html',
                      {'submissions':submissions,'all': range(1, submissions.count() // limit + 1),'user':request.user})

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
            return Response(ser.data)
        else:
            return Response(ser.errors)


class SubmissionView(APIView):
    authentication_classes = [NormalUserAuthentication, ]
