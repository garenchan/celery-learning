from celery import Celery


app = Celery('tasks',
             backend='amqp://agent:agent@172.18.231.134:5672',
             broker='amqp://agent:agent@172.18.231.134:5672')

app.conf.update(broker_connection_timeout=4.0, broker_connection_max_retries=3)


@app.task
def add(x, y):
    return x + y