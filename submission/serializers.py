from rest_framework import serializers

from submission.models import Submission, JudgeStatus


class SubmissionSerializer(serializers.ModelSerializer):
    #result = serializers.CharField(source="get_result")
    user = serializers.CharField(source="user.username")
    language = serializers.CharField(source='get_language')

    class Meta:
        model = Submission

        #fields = "__all__"

        exclude = ('contest', 'code',)

        depth = 0


class SubmissionDeserializer(serializers.ModelSerializer):
    language = serializers.IntegerField(required=True)
    code = serializers.CharField(required=True)

    class Meta:
        model = Submission

        fields = ('problem', 'language', 'code')

    def save(self, user):
        self.instance = Submission()
        self.instance.user = user
        return super().save()
