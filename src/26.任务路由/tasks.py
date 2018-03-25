import datetime
from tzlocal import get_localzone

from celery import Celery


app = Celery('tasks',
             backend='amqp://agent:agent@172.18.231.134:5672',
             broker='amqp://agent:agent@172.18.231.134:5672')
            
            
app.conf.timezone = get_localzone().zone


@app.task
def add_interval(x, y):
    return x + y


@app.task
def add_crontab(x, y):
    print('Run at:{0}'.format(datetime.datetime.now()))
    return x + y