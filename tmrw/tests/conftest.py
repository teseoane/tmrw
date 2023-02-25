import pytest
from rest_framework.test import APIClient

from tmrw.tests.users.factories import UserFactory
from tmrw.users.models import Priority


@pytest.fixture()
def client():
    return APIClient()


@pytest.fixture()
def user():
    return UserFactory(profile__priority=Priority.HIGH)
