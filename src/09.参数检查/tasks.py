from celery import Celery


app = Celery('tasks',
             backend='amqp://agent:agent@172.18.231.134:5672',
             broker='amqp://agent:agent@172.18.231.134:5672')
             

@app.task
def add(x, y):
    return x + y
    
    
# Set typing to False to disable Argument Checking
@app.task(typing=False)
def sub(x, y):
    return x - y