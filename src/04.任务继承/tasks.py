from celery import Celery
from celery import Task
import time

app = Celery('tasks',
             backend='amqp://agent:agent@172.18.231.134:5672',
             broker='amqp://agent:agent@172.18.231.134:5672')
             
             
class DebugTask(Task):


    def __call__(self, *args, **kwargs):
        print('TASK STRATING: {0.name}[{0.request.id}]'.format(self))
        return super(DebugTask, self).__call__(*args, **kwargs)
        

@app.task(base=DebugTask)
def add(x, y):
    return x + y

    
@app.task
def test_task_time_limit():
    time.sleep(4)
    
    
@app.task
def raise_error():
    raise Exception('Test raise exception')