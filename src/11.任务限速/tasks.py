from celery import Celery


app = Celery('tasks',
             backend='amqp://',
             broker='amqp://')


# Limit this task be done by a worker instance at most 10 times per minute.
# If we want to limit the times a task be done by all workers, this option not works
# Note: rate_limits can be specified in seconds, minutes or hours by appending "/s", "m" or "h" to the value.
@app.task(name='tasks.add', rate_limit='10/m')
def add(x, y):
    return x + y


if __name__ == '__main__':
    async_results = []
    for i in range(40):
        async_results.append(add.delay(i, i))