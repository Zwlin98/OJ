from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from submission.models import Submission
from .serializers import SubmissionSerializer


# Create your views here.
class SubmissionListView(APIView):

    def get(self, request, *args, **kwargs):
        submissions = Submission.objects.all()
        print(submissions[0].create_time)
        ser = SubmissionSerializer(submissions, many=True)
        return Response(ser.data)


class SubmissionView(APIView):
    pass
