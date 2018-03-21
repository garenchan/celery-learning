from celery import Celery
from celery import Task
import time

app = Celery('tasks',
             backend='amqp://agent:agent@172.18.231.134:5672',
             broker='amqp://agent:agent@172.18.231.134:5672')
             

@app.task(bind=True)
def add(self, x, y):
    print('TASK STRATING: {0.name}[{0.request.id}]'.format(self))
    return x + y