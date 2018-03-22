import logging
import sys

from celery import Celery
from celery.utils.log import get_task_logger


def get_logger():
    logger = get_task_logger('tasks')
    
    # log format
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s %(message)s')
    
    # file log
    file_handler= logging.FileHandler('tasks.log')
    file_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)
    return logger
    
logger = get_logger()


app = Celery('tasks',
             backend='amqp://agent:agent@172.18.231.134:5672',
             broker='amqp://agent:agent@172.18.231.134:5672')
             

@app.task
def add(x, y):
    logger.info('Adding {0} + {1}'.format(x, y))
    return x + y