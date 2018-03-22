from celery import Celery, Task
from celery import states


app = Celery('tasks',
             backend='amqp://agent:agent@172.18.231.134:5672',
             broker='amqp://agent:agent@172.18.231.134:5672')
             

# after_return alwayz be called no matter task success or failed
# on_retry be called on retry
# on_failure be called on failed
class MyTask(Task):
    
    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        """ Handler called after the task returns.
            Parameters: status – Current task state.
                        retval – Task return value/exception.
                        task_id – Unique id of the task.
                        args – Original arguments for the task that returned.
                        kwargs – Original keyword arguments for the task that returned
            Keyword Arguments:
                        einfo – ExceptionInfo instance, containing the traceback (if any).
        """
        print('AFTER_RETURN, status:{0},retval:{1},task_id:{2},args:{3}'.format(status, retval, task_id, args))
    
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        """ This is run by the worker when the task fails.
            Parameters: exc – The exception raised by the task.
                        task_id – Unique id of the failed task.
                        args – Original arguments for the task that failed.
                        kwargs – Original keyword arguments for the task that failed.
            Keyword Arguments:
                        einfo – ExceptionInfo instance, containing the traceback.
        """
        print('ON_FAILURE, exc:{0},task_id:{1}'.format(exc, task_id))
        
    def on_retry(self, exc, task_id, args, kwargs, einfo):
        """ This is run by the worker when the task is to be retried.
            Parameters: exc – The exception sent to retry().
                        task_id – Unique id of the retried task.
                        args – Original arguments for the retried task.
                        kwargs – Original keyword arguments for the retried task.
            Keyword Arguments:
                        einfo – ExceptionInfo instance, containing the traceback.
        """
        print('ON_RETRY, exc:{0},task_id:{1}'.format(exc, task_id))
        

@app.task(base=MyTask, bind=True, max_retries=2)
def test_task_handler(self, command):
    if command == states.SUCCESS:
        return command
    elif command == states.FAILURE:
        raise ZeroDivisionError()
    elif command == states.RETRY:
        self.retry(exc=ZeroDivisionError(), countdown=5)