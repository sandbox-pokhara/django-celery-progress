from celery.result import AsyncResult


def get_job_info(obj, key):
    try:
        if obj.date_completed is not None:
            return None
        job = AsyncResult(str(obj.uuid))
        return job.info[key]
    except (TypeError, KeyError):
        return None
