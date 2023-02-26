from rest_framework import generics, viewsets

from tmrw.jobs.api.serializers import JobSerializer, JobSubmissionSerializer
from tmrw.jobs.models import Job, JobSubmission
from tmrw.jobs.services import JobManager


class JobListView(generics.ListAPIView):
    queryset = Job.objects.all().order_by('name')
    serializer_class = JobSerializer


class JobSubmissionViewSet(viewsets.ModelViewSet):
    serializer_class = JobSubmissionSerializer

    def get_queryset(self):
        return JobSubmission.objects.filter(user=self.request.user).order_by('id')

    def perform_create(self, serializer):
        job_submission = serializer.save()
        JobManager().schedule_job(job_submission)
        return job_submission
