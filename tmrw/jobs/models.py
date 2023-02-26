from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Job(models.Model):
    name = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return f'Job({self.pk}): {self.name}'


class JobSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    duration = models.PositiveIntegerField()

    started_at = models.DateTimeField(null=True, blank=True)
    finished_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'ID: {self.pk} - Job: {self.job.name} - User: {self.user.username}'
