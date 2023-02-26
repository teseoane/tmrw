from rest_framework import serializers

from tmrw.jobs.models import Job, JobSubmission


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'name']


class JobSubmissionSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = JobSubmission
        fields = ['id', 'user', 'job', 'duration']
