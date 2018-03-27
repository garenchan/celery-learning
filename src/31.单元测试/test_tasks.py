# coding=utf-8
from __future__ import absolute_import, unicode_literals

from .conftest import try_more
from .tasks import add, sleeping, delayed_sum, delayed_sum_with_soft_guard, retry_once


class TestTasks(object):

    @try_more
    def test_task_acccepted(self, manager, sleep=1):
        r1 = sleeping.delay(2)
        manager.assert_accepted([r1.id])
        
    @try_more
    def test_task_retried(self, celery_session_worker):
        with celery_session_worker:
            assert retry_once.delay().get(timeout=10) == 1

