from rest_framework import generics

from tmrw.jobs.api.serializers import JobSerializer
from tmrw.jobs.models import Job


class JobListView(generics.ListAPIView):
    queryset = Job.objects.all().order_by('name')
    serializer_class = JobSerializer
