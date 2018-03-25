from celery import Celery
from kombu import Exchange, Queue, binding


app = Celery('tasks',
             backend='amqp://agent:agent@172.18.231.134:5672',
             broker='amqp://agent:agent@172.18.231.134:5672')
            
task_exchange = Exchange('tasks', type='direct')
logs_exchange = Exchange('logs', type='fanout')

app.conf.task_queues = [
    Queue('tasks', task_exchange, routing_key='tasks'),
    Queue('logs', logs_exchange)
]

app.conf.task_routes = {
    'tasks.add': {
        'exchange': 'tasks',
        'routing_key': 'tasks',
    },
    'tasks.log': {
        'exchange': 'logs'
    }
}


@app.task
def add(x, y):
    return x + y


@app.task
def log(level, message):
    print('[{0}]: {1}'.format(level, message))