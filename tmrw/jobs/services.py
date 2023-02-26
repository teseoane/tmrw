from django.conf import settings

from tmrw.jobs.tasks import task_process_job
from tmrw.users.models import Priority


class JobManager(object):
    """
    Class to handle job submissions execution and priorities.
    """

    def _get_priority_queue(self, job_submission):
        """
        Determines the priority queue based on the user profile priority.
        """
        match job_submission.user.profile.priority:
            case Priority.HIGH:
                return settings.QUEUE_HIGH
            case Priority.MEDIUM:
                return settings.QUEUE_MEDIUM
            case _:
                return settings.QUEUE_LOW

    def schedule_job(self, job_submission):
        task_process_job.apply_async(
            args=[job_submission.pk],
            queue=self._get_priority_queue(job_submission),
        )
