import pytest

from tmrw.tests.jobs.factories import JobFactory, JobSubmissionFactory


@pytest.fixture()
def job():
    return JobFactory()


@pytest.fixture()
def jobs():
    return JobFactory.create_batch(5)


@pytest.fixture()
def job_submission():
    return JobSubmissionFactory()
