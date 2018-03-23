from celery import Celery


app = Celery('tasks',
             backend='amqp://agent:agent@172.18.231.134:5672',
             broker='amqp://agent:agent@172.18.231.134:5672')


@app.task(bind=True)
def add(self, x, y):
    print(self.request.id)
    return x + y
