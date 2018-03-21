from celery import Celery

app = Celery(__name__, 
             backend='amqp://agent:agent@172.18.231.134:5672',
             broker='amqp://agent:agent@172.18.231.134:5672')

@app.task
def add(x, y):
    return x + y

    
@app.task
def raise_error():
    raise Exception('Test raise exception')