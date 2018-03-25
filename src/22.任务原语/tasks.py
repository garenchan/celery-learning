from celery import Celery


app = Celery('tasks',
             backend='amqp://agent:agent@172.18.231.134:5672',
             broker='amqp://agent:agent@172.18.231.134:5672')


@app.task
def add(x, y):
    return x + y


@app.task
def xsum(args):
    return sum(args)


@app.task
def raise_error():
    raise Exception('Something Error')


@app.task
def on_chord_error(request, exc, traceback):
    print('Task {0!r} raised error: {1!r}'.format(request.id, exc))