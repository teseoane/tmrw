import pytest


@pytest.mark.django_db
def test_job__str__(job):
    job.name = 'Some Cool Job Name'
    job.save()

    assert job.__str__() == f'Job({job.pk}): Some Cool Job Name'


@pytest.mark.django_db
def test_job_submission__str__(job_submission):
    job_submission.job.name = 'CoolJob'
    job_submission.job.save()
    job_submission.user.username = 'Goro'
    job_submission.user.save()

    assert job_submission.__str__() == f'ID: {job_submission.pk} - Job: CoolJob - User: Goro'
