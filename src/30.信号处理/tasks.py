from celery import Celery
# publisher signals
from celery.signals import before_task_publish, after_task_publish 
# consumers signals
from celery. signals import task_prerun, task_success

app = Celery('tasks',
             backend='amqp://agent:agent@172.18.231.134:5672',
             broker='amqp://agent:agent@172.18.231.134:5672')
            
            
#NOTE: I think it's better to call it hooks and easy to understand!

@app.task
def add(x, y):
    result = x + y
    return result
    

@before_task_publish.connect
def before_task_publish_handler(sender=None, body=None, **kwargs):
    print('BEFORE_TASK_PUBLISH: {0}, {1}, {2}'.format(sender, body, kwargs))
    
    
@after_task_publish.connect
def after_task_publish_handler(sender=None, headers=None, body=None, **kwargs):
    print('AFTER_TASK_PUBLISH: {0}, {1}, {2}, {3}'.format(sender, headers, body, kwargs))
    

@task_prerun.connect
def task_prerun_handler(sender=None, task_id=None, **kwargs):
    print('TASK_PRERUN: {0}, {1}, {2}'.format(sender, task_id, kwargs))
    
    
@task_success.connect
def task_success_handler(sender=None, result=None, **kwargs):
    print('TASK_SUCCESS: {0}, {1}, {2}'.format(sender, result, kwargs))