from celery import Celery
from celery import Task
import time

app = Celery('tasks',
             backend='amqp://agent:agent@172.18.231.134:5672',
             broker='amqp://agent:agent@172.18.231.134:5672')
             

@app.task(bind=True)
def add(self, x, y):
    for attr in dir(self.request):
        if not attr.startswith('__'):
            print('{0} = {1}'.format(attr, getattr(self.request, attr, None)))
            
    # self.request is a instance of app.Task.Request
    # 
    # The request defines the following attributes:
    #   id:             The unique id of the executing task.
    #   group:          The unique id of the task’s group, if this task is a member.
    #   chord:          The unique id of the chord this task belongs to (if the task is part of the header).
    #   correlation_id: Custom ID used for things like de-duplication.
    #   args:           Positional arguments.
    #   kwargs:         Keyword arguments.
    #   origin:         Name of host that sent this task.
    #   retries:        How many times the current task has been retried. An integer starting at 0.
    #   is_eager:       Set to True if the task is executed locally in the client, not by a worker.
    #   eta:            The original ETA of the task (if any). This is in UTC time (depending on the enable_utc setting).
    #   expires:        The original expiry time of the task (if any). This is in UTC time (depending on the enable_utc setting).
    #   hostname:       Node name of the worker instance executing the task.
    #   delivery_info:  Additional message delivery information. This is a mapping containing the exchange 
    #                   and routing key used to deliver this task. Used by for example app.Task.retry() 
    #                   to resend the task to the same destination queue. #Availability of keys in this dict 
    #                   depends on the message broker used.
    #   called_directly:This flag is set to true if the task wasn’t executed by the worker.
    #   timelimit:      A tuple of the current (soft, hard) time limits active for this task (if any).
    #   callbacks:      A list of signatures to be called if this task returns successfully.
    #   errback:        A list of signatures to be called if this task fails.
    #   utc:            Set to true the caller has UTC enabled (enable_utc).
    #   headers:        Mapping of message headers sent with this task message (may be None).
    #   reply_to:       Where to send reply to (queue name).
    #   root_id:        The unique id of the first task in the workflow this task is part of (if any).
    #   parent_id:      The unique id of the task that called this task (if any).
    #   chain:          Reversed list of tasks that form a chain (if any). The last item in this list 
    #                   will be the next task to succeed the current task. If using version one of the 
    #                   task protocol the chain tasks will be in request.callbacks instead.
    return x + y