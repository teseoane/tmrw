import pytest


@pytest.mark.django_db
def test_profile__str__(user):
    user.username = 'Goro'
    user.save()
    assert user.profile.__str__() == f'Profile({user.profile.pk}) - User: Goro'
