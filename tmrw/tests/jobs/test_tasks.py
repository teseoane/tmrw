import pytest
from freezegun import freeze_time

from tmrw.jobs.tasks import task_process_job


@pytest.mark.django_db
@freeze_time('2022-01-14 0:00:00')
def test_task_process_job(mocker, job_submission):
    mocker.patch('tmrw.jobs.tasks.logger.info', return_value=None)

    job_submission.duration = 0
    job_submission.save()

    task_process_job(job_submission.pk)
    job_submission.refresh_from_db()

    assert str(job_submission.started_at) == '2022-01-14 00:00:00'
    assert str(job_submission.finished_at) == '2022-01-14 00:00:00'
