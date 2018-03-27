# coding=utf-8
from __future__ import absolute_import, unicode_literals

import time

from celery import shared_task
from celery.exceptions import SoftTimeLimitExceeded
from celery.utils.log import get_task_logger
            
logger = get_task_logger(__name__)
            
            
@shared_task
def add(x, y):
    """Add two numbers."""
    return x + y
    
    
@shared_task
def sleeping(stime):
    time.sleep(stime)
    

@shared_task
def delayed_sum(numbers, paused_time=1):
    """Sum the iterable of numbers."""
    time.sleep(paused_time)
    return sum(numbers)
    
    
@shared_task
def delayed_sum_with_soft_guard(numbers, paused_time=1):
    """Sum the iterable of numbers."""
    try:
        time.sleep(paused_time)
    except SoftTimeLimitExceeded:
        return 0
    else:
        return sum(numbers)
        
        
@shared_task(bind=True, expires=60.0, max_retries=1)
def retry_once(self):
    if self.request.retries:
        return self.request.retries
    raise self.retry(countdown=0.1)
