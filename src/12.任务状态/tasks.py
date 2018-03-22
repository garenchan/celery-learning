from celery import Celery
from celery import states
import time

app = Celery('tasks',
             backend='amqp://agent:agent@172.18.231.134:5672',
             broker='amqp://agent:agent@172.18.231.134:5672')
             
# Built-in State
#   PENDING: Task is waiting for execution or unknown. Any task id that's not known is implied to be 
#            in the pending state.
#   STARTED: Task has been started. Not reported by default, to enable please see app.Task.track_started.
#            meta-data:  pid and hostname of the worker process executing the task.
#   SUCCESS: Task has been successfully executed.
#            meta-data:  result contains the return value of the task.
#            propagates: Yes
#            ready:      Yes
#   FAILURE: Task execution resulted in failure.
#            meta-data:  result contains the exception occurred, and traceback contains the backtrace 
#                        of the stack at the point when the exception was raised.
#            propagates: Yes
#   RETRY:   Task is being retried.
#            meta-data:  result contains the exception that caused the retry, and traceback contains
#                        the backtrace of the stack at the point when the exceptions was raised.
#            propagates: No
#   REVOKED: Task has been revoked.
#            propagates: Yes
             
@app.task(bind=True)
def track_task_state(self):
    time.sleep(20)
    self.update_state(state=states.STARTED)
    time.sleep(20)
             
             
@app.task(bind=True)
def track_task_state_with_custom(self):
    custom_states = ['BEGINNED', 'PROGRESS', 'FINISHED']
    for state in custom_states:
        self.update_state(state=state, meta={'track_state': state})
        time.sleep(20)
        

