import os

from celery import Celery


CUR_DIR = os.path.abspath(__file__)
DIR_NAME = os.path.dirname(CUR_DIR)

app = Celery('tasks',
             backend='amqp://agent:agent@172.18.231.134:5672',
             broker='amqp://agent:agent@172.18.231.134:5672')

app.conf.update(
    security_key=os.path.join(DIR_NAME, 'ssl', 'server.key'),
    security_certificate=os.path.join(DIR_NAME, 'ssl', 'server.crt'),
    security_cert_store=os.path.join(DIR_NAME, 'ssl', '*.crt')
)
# we need to set task_serializer to 'auth', it's important.
# or else setup_security function do nothing.
app.conf.task_serializer = 'auth'

app.setup_security()


@app.task(bind=True)
def add(self, x, y):
    return x + y