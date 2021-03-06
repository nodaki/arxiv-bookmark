from celery import Celery
from celery.schedules import crontab

app = Celery("worker")
app.config_from_object("worker.celeryconfig")
app.conf.enable_utc = False

app.conf.beat_schedule = {
        "create-and-update-papers": {
                "task": "worker.papers.create_and_update_papers",
                "schedule": crontab(minute=0, hour=23)
        }
}

if __name__ == '__main__':
    app.start()
