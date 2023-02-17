# Django Celery Monitor

A django app to monitor celery tasks with progress

## Quick start

Add "django_celery_progress" to your INSTALLED_APPS:

```
    INSTALLED_APPS = [
        'django_celery_progress',
    ]
```

Set CELERY_BROKER_URL and CELERY_RESULT_BACKEND

```
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
```

## Progress monitor:

```
import time

from celery import shared_task
from django_celery_progress.progress import set_progress

@shared_task(bind=True, name='my_task')
def my_task(self):
    for i in range(100):
        time.sleep(1)
        set_progress(self, i + 1, 100)
```

## Screenshot

![Screenshot](https://raw.githubusercontent.com/sandbox-pokhara/django-celery-progress/master/images/screenshot.png)
