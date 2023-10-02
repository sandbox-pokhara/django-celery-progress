from django.contrib import admin
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.urls import path
from django.urls.resolvers import URLPattern

from django_celery_progress.models import Task
from django_celery_progress.utils import get_job_info
from django_celery_progress.views import progress


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    change_list_template = "django_celery_progress/change_list.html"

    list_display = [
        "id",
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

    date_created_natural.short_description = "Date Created"
    date_completed_natural.short_description = "Date Completed"

    date_created_natural.admin_order_field = "date_created"
    date_completed_natural.admin_order_field = "date_completed"

    def has_add_permission(self, *args, **kwargs):
        return False

    def has_change_permission(self, *args, **kwargs):
        return False

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path(
                "<int:task_id>/progress/",
                self.admin_site.admin_view(progress),
            )
        ]
        return my_urls + urls
