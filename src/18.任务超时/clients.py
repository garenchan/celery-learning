from datetime import datetime, timedelta
import time

from celery import states

from tasks import app, add


# NOTE: After run client, wait 15 seconds and run a worker
if __name__ == '__main__':
    async_results = []
    async_results.append(add.apply_async((2, 3), expires=10))
    
    # You must be careful when use datetime as expire time.
    # Because Celery default use UTC timezone
    dt = datetime.now(app.timezone) + timedelta(seconds=10)
    async_results.append(add.apply_async((2, 3), expires=dt))
    
    time.sleep(30)
    for result in async_results:
        print('{0}: {1}, {2}'.format(result.task_id, result.state, result.result))
        assert result.state == states.REVOKED


