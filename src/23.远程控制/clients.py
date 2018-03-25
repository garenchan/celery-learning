import time

from tasks import app, add, xsum, long_task


if __name__ == '__main__':
    reply = app.control.broadcast('rate_limit', {
        'task_name': 'tasks.add',
        'rate_limit': '10/m'
    }, reply=True)
    print('Reply: %s' % reply)
    
    
    # revoke a task
    result = long_task.delay()
    time.sleep(3)
    # below is equal to: result.revoke()
    app.control.revoke(result.task_id, terminate=True)
    
    # time limit don’t currently work on platforms that don’t support the SIGUSR1 signal.
    # so it cannot work on Windows.
    reply = app.control.time_limit('tasks.long_task', soft=10, hard=20, reply=True)
    print('Reply: %s' % reply)
    long_task.apply_async()
    
    
    # add consumer
    reply = app.control.add_consumer(
        queue='baz',
        exchange='ex',
        exchange_type='topic',
        routing_key='media.*',
        options={
            'queue_durable': False,
            'exchange_durable': False,
        },
        reply=True
    )
    print('Reply: %s' % reply)
    
    # inspect workers
    reply = app.control.inspect()
    print('Active tasks: %s' % reply.active())
    
    # ping workers
    reply = app.control.ping(timeout=0.5)
    print('Reply: %s' % reply)
    
    # warm shutdown all workers
    reply = app.control.broadcast('shutdown')
    print('Reply: %s' % reply)