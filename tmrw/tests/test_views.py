import pytest
from django.test import RequestFactory

pytestmark = pytest.mark.django_db


def test_status_view(client: RequestFactory):
    response = client.get('/__status__/')
    json_response = response.json()

    assert json_response['status'] == 'OK'
    assert type(json_response['timestamp']) is float
