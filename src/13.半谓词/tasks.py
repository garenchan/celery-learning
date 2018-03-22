from celery import Celery
from celery.exceptions import Ignore, Reject, Retry
from celery import states

app = Celery('tasks',
             backend='amqp://agent:agent@172.18.231.134:5672',
             broker='amqp://agent:agent@172.18.231.134:5672')
             

             
@app.task(bind=True)
def div_ignore_zero(self, x, y):
    if y == 0:
        self.update_state(state=states.SUCCESS)
        raise Ignore()
    return x / y
        

@app.task
def div_reject_zero(x, y):
    try:
        ret = x / y
    except Exception as exc:
        # If enable re-queue, may lead to a infinite message loop
        raise Reject(str(exc), requeue=False)
    else:
        return ret
    
    
@app.task(max_retries=2)
def div_retry(x, y):
    try:
        ret = x / y
    except Exception as exc:
        raise Retry(exc=exc, when=5)
    else:
        return ret

