from celery.result import AsyncResult
from django.contrib import admin
from django.contrib.humanize.templatetags.humanize import naturaltime

from .models import Task


def get_job_info(obj, key):
    try:
        if obj.date_completed is not None:
            return None
        job = AsyncResult(str(obj.uuid))
        return job.info[key]
    except (TypeError, KeyError):
        return None


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "status",
        "current",
        "total",
        "result",
        "exception",
        "date_created_natural",
        "date_completed_natural",
    ]

    list_filter = [
        "name",
        "status",
        "exception",
        "date_created",
        "date_completed",
    ]

    search_fields = [
        "uuid",
        "name",
        "status",
        "result",
        "exception",
        "traceback",
    ]

    def current(self, obj):
        return get_job_info(obj, "current")

    def total(self, obj):
        return get_job_info(obj, "total")

    def date_created_natural(self, obj):
        return naturaltime(obj.date_created)

    def date_completed_natural(self, obj):
        return naturaltime(obj.date_completed)

    def has_add_permission(self, *args, **kwargs):
        return False

    def has_change_permission(self, *args, **kwargs):
        return False

    date_created_natural.short_description = "Date Created"
    date_completed_natural.short_description = "Date Completed"

    date_created_natural.admin_order_field = "date_created"
    date_completed_natural.admin_order_field = "date_completed"
