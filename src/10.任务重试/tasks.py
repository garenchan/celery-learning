from celery import Celery
import requests
import uuid

app = Celery('tasks',
             backend='amqp://agent:agent@172.18.231.134:5672',
             broker='amqp://agent:agent@172.18.231.134:5672')
             
             
# Just retry, default retry in 180s
@app.task(bind=True)
def retry_without_limit(self):
    try:
        ret = 1 / 0
    except Exception as exc:
        raise self.retry(exc=exc)

        
# Retry in custom delay
@app.task(bind=True, default_retry_delay=30)
def retry_with_custome_delay(self):
    try:
        ret = 1 / 0
    except Exception as exc:
        # override default use countdown
        raise self.retry(exc=exc, countdown=60)

        
# Max retries, after that if task still not finished, the exception will raise
@app.task(bind=True, max_retries=3, default_retry_delay=10)
def retry_with_max_times(self):
    try:
        ret = 1 / 0
    except Exception as exc:
        raise self.retry(exc=exc)
        

# Auto retry for known exceptions, and specify custome arguments for internal retry call
@app.task(autoretry_for=(ZeroDivisionError,), 
          retry_kwargs={'max_retries': 2, 'countdown': 5})
def retry_with_know_exceptions():
    ret = 1 / 0

        
# Use Exponential Backoff with retry
# It's new in version 4.1, but we use 4.0.2, so it won't make a difference, emmmmm!
@app.task(autoretry_for=(requests.exceptions.ConnectionError,), 
          retry_backoff=True)
def retry_with_exp_backoff():
       url = 'http://www.{0}.com'.format(uuid.uuid4().hex)
       response = requests.get(url)

