from tasks import app
from datetime import timedelta

beat_schedule = {
    # 每10s执行一次任务tasks.add
    'add': {
        'task': 'tasks.add',
        'schedule': timedelta(seconds=10),
        'args': (2, 3),
    }
}

app.conf.update(beat_schedule=beat_schedule)