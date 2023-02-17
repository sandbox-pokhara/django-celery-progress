from django.apps import AppConfig


class DjangoCeleryProgressConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_celery_progress'
    verbose_name = 'Celery Tasks'
