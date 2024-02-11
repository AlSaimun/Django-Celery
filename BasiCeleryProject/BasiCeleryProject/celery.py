import os

from celery import Celery
import time
from celery.schedules import crontab



# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BasiCeleryProject.settings')

app = Celery('BasiCeleryProject')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'add_task' : {
        'task' : 'myapp.tasks.add',
        'schedule' : crontab(minute='*/1'), # also can hour, day_of_week, month_of_year, day_of_month
        'args' : (10, 50), 
    }
}


@app.task(name='My_subb_Task')
def subb(x, y):
    time.sleep(10)
    return x - y

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')