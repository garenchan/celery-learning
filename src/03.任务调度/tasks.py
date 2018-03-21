from celery import Celery
import time

app = Celery('tasks',
             backend='amqp://agent:agent@172.18.231.134:5672',
             broker='amqp://agent:agent@172.18.231.134:5672')

@app.task
def add(x, y):
    return x + y

@app.task
def test_task_time_limit():
    time.sleep(4)
    
    
@app.task
def raise_error():
    raise Exception('Test raise exception')