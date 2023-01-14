from celery import Celery, Task
from flask import current_app as app
from celery.schedules import crontab

celery = Celery("Jobs", broker='redis://localhost:6379/0', backend='redis://localhost:6379/1',imports=["mail.daily_reminder"])
celery.conf.timezone = 'Asia/Kolkata'


class ContextTask(Task):
    def __call__(self, *args, **kwargs):
        with app.app_context():
            return self.run(*args, **kwargs)

