from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Priority(models.TextChoices):
    HIGH = 'high', _('High')
    MEDIUM = 'medium', _('Medium')
    LOW = 'low', _('Low')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    priority = models.CharField(max_length=6, choices=Priority.choices)

    def __str__(self):
        return f'Profile({self.pk}) - User: {self.user.username}'
