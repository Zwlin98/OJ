from rest_framework import serializers

from submission.models import Submission, JudgeStatus


class SubmissionSerializer(serializers.ModelSerializer):

    result = serializers.CharField(source="get_result")
    user = serializers.CharField(source="user.username")
    language = serializers.CharField(source='get_language')

    class Meta:
        model = Submission

        # fields = "__all__"

        exclude = ('contest',)

        depth = 0
