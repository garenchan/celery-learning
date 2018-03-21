from celery import Celery
import time

app = Celery(__name__, 
             backend='amqp://agent:agent@172.18.231.134:5672',
             broker='amqp://agent:agent@172.18.231.134:5672')
             
app.config_from_object('celeryconfig')
             

@app.task
def add(x, y):
    return x + y

@app.task
def test_task_time_limit():
    time.sleep(4)
    
    
@app.task
def raise_error():
    raise Exception('Test raise exception')