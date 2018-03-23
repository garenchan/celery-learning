import time

from celery import Celery


app = Celery('tasks',
             backend='amqp://agent:agent@172.18.231.134:5672',
             broker='amqp://agent:agent@172.18.231.134:5672')


@app.task(bind=True)
def track_states(self, x, y):
    time.sleep(5)
    self.update_state(state='PROGRESS', meta={'progress': 50})
    time.sleep(5)
    self.update_state(state='PROGRESS', meta={'progress': 80})
    time.sleep(3)
    return 'hello world: %i' % (x + y)
