import time 

from celery import Celery
from celery.worker.control import control_command, inspect_command
from celery.exceptions import SoftTimeLimitExceeded

app = Celery('tasks',
             backend='amqp://agent:agent@172.18.231.134:5672',
             broker='amqp://agent:agent@172.18.231.134:5672')
             

@control_command(args=[('n', int)], signature='[N=1]')
def increase_prefetch_count(state, n=1):
    state.consumer.qos.increment_eventually(n)
    return {'ok': 'prefetch count incremented'}
    

'''@inspect_command
def current_prefetch_count(state):
    return {'prefetch_count': state.consumer.qos.value}
'''

@app.task
def add(x, y):
    return x + y


@app.task
def xsum(args):
    return sum(args)
    

@app.task(bind=True)
def long_task(self):
    try:
        for i in range(100):
            print('%s: %s' % (self.request.id, i))
            time.sleep(10)
    except SoftTimeLimitExceeded as ex:
        print(ex)
        for j in range(i + 1, 100):
            time.sleep(10)