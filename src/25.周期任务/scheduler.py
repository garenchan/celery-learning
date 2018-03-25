from datetime import timedelta

from celery.schedules import crontab

from tasks import app

beat_schedule = {
    # 每10s执行一次任务tasks.add
    'add_interval': {
        'task': 'tasks.add_interval',
        'schedule': timedelta(seconds=10), # '10'
        'args': (2, 3),
    },
    'add_crontab': {
        'task': 'tasks.add_crontab',
        'schedule': crontab(hour=21, minute=32),
        'args': (3, 4),
    }
}

app.conf.update(beat_schedule=beat_schedule)