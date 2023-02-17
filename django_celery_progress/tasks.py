import time
import traceback as tb

from celery import shared_task
from celery.signals import task_failure
from celery.signals import task_postrun
from celery.signals import task_prerun
from celery.signals import task_received
from django.conf import settings
from django.utils import timezone

from .models import Task
from .progress import set_progress


@task_received.connect
def task_received_handler(request, **kwargs):
    del kwargs
    info = request.info()
    task, _ = Task.objects.get_or_create(uuid=info['id'])
    task.status = 'RECEIVED'
    task.name = info['name']
    task.save()


@task_prerun.connect
def task_prerun_handler(task_id, **kwargs):
    del kwargs
    task, _ = Task.objects.get_or_create(uuid=task_id)
    task.status = 'RUNNING'
    task.save()


@task_postrun.connect
def task_postrun_handler(task_id, retval, state, **kwargs):
    del kwargs
    task, _ = Task.objects.get_or_create(uuid=task_id)
    task.status = state
    task.result = retval
    task.date_completed = timezone.now()
    task.save()


@task_failure.connect
def task_failure_handler(task_id, exception, traceback, **kwargs):
    del kwargs
    task, _ = Task.objects.get_or_create(uuid=task_id)
    task.exception = exception.__class__.__name__
    task.traceback = ''.join(tb.format_tb(traceback))
    task.save()


@shared_task(name='remove-old-tasks')
def remove_old_tasks():
    if not hasattr(settings, 'CELERY_MAX_TASKS'):
        return 'CELERY_MAX_TASKS is not set.'
    to_remove = Task.objects.order_by('-id')[settings.CELERY_MAX_TASKS:]
    count, _ = Task.objects.filter(pk__in=to_remove.values_list('pk', flat=True)).delete()
    return f'{count} task(s) removed.'


@shared_task(bind=True, name='my_task')
def my_task(self):
    for i in range(100):
        time.sleep(1)
        set_progress(self, i + 1, 100)
