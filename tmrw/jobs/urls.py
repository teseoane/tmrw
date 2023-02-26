from django.urls import path
from rest_framework.routers import DefaultRouter

from tmrw.jobs.api.views import JobListView, JobSubmissionViewSet

router = DefaultRouter()

urlpatterns = [
    path('', JobListView.as_view(), name='jobs-list'),
]

router.register(r'job-submissions', JobSubmissionViewSet, basename='job-submissions')

urlpatterns += router.urls
