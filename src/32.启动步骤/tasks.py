from celery import Celery

from my_bootsteps import ExampleWorkerStep, DeadlockDetectionStep

app = Celery('tasks',
             backend='amqp://agent:agent@172.18.231.134:5672',
             broker='amqp://agent:agent@172.18.231.134:5672')

# add custom options
def add_worker_arguments(parser):
    parser.add_argument('--enable-my-option', action='store_true',
        default=False, help='Enable custom option.')

app.user_options['worker'].add(add_worker_arguments)
        
app.steps['worker'].update([ExampleWorkerStep, DeadlockDetectionStep])
             
@app.task
def add(x, y):
    return x + y

