import logging
import time
from datetime import datetime

from celery import shared_task

from tmrw.jobs.models import JobSubmission

logger = logging.getLogger(__name__)


@shared_task
def task_process_job(job_submission_pk):
    logger.info(f'Starting processing job_submission: {job_submission_pk}')

    job_submission = JobSubmission.objects.get(pk=job_submission_pk)
    job_submission.started_at = datetime.now()
    time.sleep(job_submission.duration)
    job_submission.finished_at = datetime.now()
    job_submission.save()

    logger.info(f'Finished processing job_submission: {job_submission_pk}')
