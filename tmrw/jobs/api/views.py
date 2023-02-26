from rest_framework import generics, viewsets

from tmrw.jobs.api.serializers import JobSerializer, JobSubmissionSerializer
from tmrw.jobs.models import Job, JobSubmission


class JobListView(generics.ListAPIView):
    queryset = Job.objects.all().order_by('name')
    serializer_class = JobSerializer


class JobSubmissionViewSet(viewsets.ModelViewSet):
    serializer_class = JobSubmissionSerializer

    def get_queryset(self):
        return JobSubmission.objects.filter(user=self.request.user).order_by('id')
