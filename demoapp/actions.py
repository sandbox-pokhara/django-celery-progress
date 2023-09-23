from django.shortcuts import redirect
from form_action import extra_button

from django_celery_progress.tasks import my_task


@extra_button("Create a demo task")
def create_demo_task(request):
    my_task.delay()
    return redirect("admin:django_celery_progress_task_changelist")
