import pytest
from django.conf import settings

from tmrw.jobs.services import JobManager
from tmrw.users.models import Priority


@pytest.mark.parametrize(
    'priority,queue_name',
    [
        (Priority.HIGH, settings.QUEUE_HIGH),
        (Priority.MEDIUM, settings.QUEUE_MEDIUM),
        (Priority.LOW, settings.QUEUE_LOW),
    ],
)
@pytest.mark.django_db
def test_job_manager__get_priority_queue(job_submission, priority, queue_name):
    job_submission.user.profile.priority = priority
    job_submission.user.profile.save()

    assert JobManager()._get_priority_queue(job_submission) == queue_name


@pytest.mark.django_db
def test_job_manager_schedule_job(mocker, job_submission):
    mock_task_process_job = mocker.patch('tmrw.jobs.services.task_process_job.apply_async')
    mocker.patch('tmrw.jobs.services.JobManager._get_priority_queue', return_value=settings.QUEUE_HIGH)

    JobManager().schedule_job(job_submission)

    mock_task_process_job.assert_called_once_with(args=[job_submission.pk], queue=settings.QUEUE_HIGH)
