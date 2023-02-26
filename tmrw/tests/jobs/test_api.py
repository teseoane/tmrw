import pytest


@pytest.mark.django_db
def test_jobs_list_ok(client, user, jobs):
    client.force_authenticate(user)

    response = client.get('/api/jobs/')

    assert response.status_code == 200
    assert len(response.data['results']) == 5


@pytest.mark.django_db
def test_job_submision_view_set_list_ok(client, user, job_submissions):
    client.force_authenticate(user)

    response = client.get('/api/jobs/job-submissions/')

    assert response.status_code == 200
    assert len(response.data['results']) == 5


@pytest.mark.django_db
def test_job_submision_view_set_retrieve_ok(client, job_submission):
    client.force_authenticate(job_submission.user)

    response = client.get(f'/api/jobs/job-submissions/{job_submission.pk}/')

    assert response.status_code == 200
    assert response.data['job'] == job_submission.job.pk
    assert response.data['duration'] == job_submission.duration


@pytest.mark.django_db
def test_job_submision_view_set_create_ok(client, user, job):
    client.force_authenticate(user)

    response = client.post(
        '/api/jobs/job-submissions/',
        {
            'job': job.pk,
            'duration': 20,
        },
    )

    assert response.status_code == 201
    assert response.data['job'] == job.pk
    assert response.data['duration'] == 20
    assert user.jobsubmission_set.count() == 1
