def set_progress(task, current, total):
    task.update_state(meta={"current": current, "total": total})
