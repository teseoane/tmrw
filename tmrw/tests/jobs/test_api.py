import pytest


@pytest.mark.django_db
def test_jobs_list_ok(client, user, jobs):
    client.force_authenticate(user)

    response = client.get('/api/jobs/')

    assert response.status_code == 200
    assert len(response.data['results']) == 5
