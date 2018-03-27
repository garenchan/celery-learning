# coding=utf-8
from __future__ import absolute_import, unicode_literals

import os
import functools

import pytest

from celery.contrib.testing.manager import Manager

TEST_BROKER = os.environ.get('TEST_BROKER', 'amqp://agent:agent@172.18.231.134:5672')
TEST_BACKEND = os.environ.get('TEST_BACKEND', 'amqp://agent:agent@172.18.231.134:5672')


def try_more(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for i in reversed(range(3)):
            try:
                return func(*args, **kwargs)
            except Exception:
                if not i:
                    raise
    return wrapper
    
    
@pytest.fixture(scope='session')
def celery_config():
    return {
        'broker_url': TEST_BROKER,
        'result_backend': TEST_BACKEND
    }
    

@pytest.fixture(scope='session')
def celery_enable_logging():
    return True
    
    
@pytest.fixture(scope='session')
def celery_worker_pool():
    return 'eventlet'
    
    
@pytest.fixture(scope='session')
def celery_includes():
    return {'.tasks'}
    
    
@pytest.fixture
def app(celery_app):
    yield celery_app
    
    
@pytest.fixture
def manager(app, celery_session_worker):
    return Manager(app)


@pytest.fixture(autouse=True)
def ZZZZ_set_app_current(app):
    app.set_current()
    app.set_default()