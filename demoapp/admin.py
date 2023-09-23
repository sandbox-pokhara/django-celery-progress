from django.contrib import admin
from form_action import ExtraButtonMixin

from demoapp.actions import create_demo_task
from django_celery_progress.admin import TaskAdmin
from django_celery_progress.models import Task

admin.site.unregister(Task)


@admin.register(Task)
class DemoTaskAdmin(ExtraButtonMixin, TaskAdmin):
    change_list_template = "demo/change_list.html"
    extra_buttons = [create_demo_task]
