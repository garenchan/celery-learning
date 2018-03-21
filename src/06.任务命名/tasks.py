from celery import Celery
from celery import Task
import uuid

app = Celery(uuid.uuid4().hex)
             

@app.task(name='custom_name')
def add(x, y):
    print('TASK STRATING: {0.name}[{0.request.id}]'.format(self))
    return x + y
    
    
@app.task
def sub(x, y):
    return x - y