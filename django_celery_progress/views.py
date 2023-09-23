from django.contrib.admin.utils import display_for_value
from django.http import JsonResponse

from django_celery_progress.models import Task
from django_celery_progress.utils import get_job_info


def progress(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        current = get_job_info(task, "current")
        total = get_job_info(task, "total")
        return JsonResponse(
            {
                "id": display_for_value(task.id, "-"),
                "status": display_for_value(task.status, "-"),
                "current": display_for_value(current, "-"),
                "total": display_for_value(total, "-"),
                "result": display_for_value(task.result, "-"),
                "exception": display_for_value(task.exception, "-"),
                "date_completed": display_for_value(task.date_completed, "-"),
            }
        )
    except Task.DoesNotExist:
        return JsonResponse({"detail": "Task does not exist."}, status=404)
