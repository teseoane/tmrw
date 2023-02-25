import factory
import factory.fuzzy
from django.contrib.auth import get_user_model

from tmrw.users.models import Priority, Profile


class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile

    priority = factory.fuzzy.FuzzyChoice(Priority.values)
    user = factory.SubFactory('tmrw.tests.users.factories.UserFactory', profile=None)


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda n: 'user_%d' % n)
    profile = factory.RelatedFactory(ProfileFactory, factory_related_name='user')

    class Meta:
        model = get_user_model()
