import pytest

from tmrw.tests.users.factories import UserFactory
from tmrw.users.models import Priority


@pytest.fixture()
def user():
    return UserFactory(profile__priority=Priority.HIGH)
