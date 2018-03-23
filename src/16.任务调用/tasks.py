from celery import Celery
from celery.result import AsyncResult

app = Celery('tasks',
             backend='amqp://agent:agent@172.18.231.134:5672',
             broker='amqp://agent:agent@172.18.231.134:5672')


@app.task
def my_add(x, y):
    return x + y


@app.task
def my_sum(*args, **kwargs):
    return sum(args)


@app.task
def my_echo(*args, **kwargs):
    return {
        '包裹位置参数': args,
        '包裹关键字参数': kwargs
    }


@app.task
def my_div(x, y):
    return x / y


@app.task
def error_handler(task_id):
    result = AsyncResult(task_id)
    exc = result.get(propagate=False)
    print('Task {0} raise error: {1}\n{2}'.format(task_id, exc, result.traceback))
