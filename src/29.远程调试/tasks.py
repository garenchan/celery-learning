from celery import Celery
from celery.contrib import rdb

app = Celery('tasks',
             backend='amqp://agent:agent@172.18.231.134:5672',
             broker='amqp://agent:agent@172.18.231.134:5672')
            


@app.task
def add(x, y):
    result = x + y
    rdb.set_trace()
    return result