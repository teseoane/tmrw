import pytest

from tmrw.jobs.api.views import JobSubmissionViewSet


@pytest.mark.django_db
def test_job_submision_view_set_get_queryset_ok(rf, user, job_submissions):
    view = JobSubmissionViewSet()
    request = rf.get('/fake')
    request.user = user
    view.action = 'list'
    view.request = request

    assert view.get_queryset().count() == 5
