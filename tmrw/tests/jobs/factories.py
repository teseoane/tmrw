import factory
import factory.fuzzy

from tmrw.jobs.models import Job, JobSubmission


class JobFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText(length=10)

    class Meta:
        model = Job
        django_get_or_create = ('name',)


class JobSubmissionFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory('tmrw.tests.users.factories.UserFactory')
    job = factory.SubFactory('tmrw.tests.jobs.factories.JobFactory')
    duration = factory.fuzzy.FuzzyInteger(0, 100)

    class Meta:
        model = JobSubmission
