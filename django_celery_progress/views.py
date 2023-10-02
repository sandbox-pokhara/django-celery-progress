from functools import partial

from django.contrib.admin.utils import display_for_value
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.http import JsonResponse

from django_celery_progress.models import Task
from django_celery_progress.utils import get_job_info


def progress(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        current = get_job_info(task, "current")
        total = get_job_info(task, "total")
        display = partial(display_for_value, empty_value_display="-")
        data = {
            "id": display(task.id),
            "status": display(task.status),
            "current": display(current),
            "total": display(total),
            "result": display(task.result),
            "exception": display(task.exception),
            "date_created": display(naturaltime(task.date_created)),
            "date_completed": display(naturaltime(task.date_completed)),
        }
        return JsonResponse(data)
    except Task.DoesNotExist:
        return JsonResponse({"detail": "Task does not exist."}, status=404)
