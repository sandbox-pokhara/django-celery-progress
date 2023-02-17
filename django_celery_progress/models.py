from django.db import models
from django.utils import timezone


class Task(models.Model):
    uuid = models.UUIDField(unique=True)
    name = models.CharField(max_length=128)
    status = models.CharField(max_length=128)
    result = models.TextField(blank=True, null=True)
    exception = models.CharField(blank=True, null=True, max_length=128)
    traceback = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField()
    date_completed = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.id is None:
            self.date_created = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.uuid)
