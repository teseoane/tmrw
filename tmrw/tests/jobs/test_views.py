import pytest

from tmrw.jobs.api.serializers import JobSubmissionSerializer
from tmrw.jobs.api.views import JobSubmissionViewSet


@pytest.mark.django_db
def test_job_submision_view_set_get_queryset_ok(rf, user, job_submissions):
    view = JobSubmissionViewSet()
    request = rf.get('/fake')
    request.user = user
    view.action = 'list'
    view.request = request

    assert view.get_queryset().count() == 5


@pytest.mark.django_db
def test_job_submision_view_set_perform_create(mocker, rf, user, job, job_submission):
    mock_schedule_job = mocker.patch('tmrw.jobs.api.views.JobManager.schedule_job')
    mocker.patch(
        'tmrw.jobs.api.views.JobSubmissionSerializer.save', return_value=job_submission
    )
    view = JobSubmissionViewSet()
    request = rf.post('/fake')
    request.user = user
    view.action = 'create'
    view.request = request

    view.perform_create(JobSubmissionSerializer())

    mock_schedule_job.assert_called_once_with(job_submission)
