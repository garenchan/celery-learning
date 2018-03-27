import time

from celery import bootsteps


class ExampleWorkerStep(bootsteps.StartStopStep):

    requires = {'celery.worker.components:Pool'}
    
    IDENT = '[ExampleWorkerStep]'
    
    def __init__(self, worker, **kwargs):
        enable_my_option = kwargs.get('enable_my_option', False)
        if enable_my_option:
            print('{0} enable my custom option'.format(self.IDENT))
        print('{0} Called when the WorkController instance is constructed'.format(self.IDENT))
        print('{0} Arguments to WorkController: {1!r}'.format(self.IDENT, kwargs))
        
    def create(self, worker):
        return self
        
    def start(self, worker):
        print('{0} Called when the worker is started.'.format(self.IDENT))
        
    def stop(self, worker):
        print('{0} Called when the worker shuts down.'.format(self.IDENT))
        
    def terminate(self, worker):
        print('{0} Called when the worker terminates'.format(self.IDENT))
        
        
class DeadlockDetectionStep(bootsteps.StartStopStep):
    
    requires = {'celery.worker.components:Timer'}
    
    IDENT = '[DeadlockDetectionStep]'
    
    def __init__(self, worker, **kwargs):
        self.timeout = kwargs.get('deadlock_timeout', 3600)
        self.requests = []
        self.tref = None
        
    def start(self, worker):
        self.tref = worker.timer.call_repeatedly(30.0, self.detect, (worker,), priority=10)
        print('{0} Called when the worker is started.'.format(self.IDENT))
        
    def stop(self, worker):
        if self.tref:
            self.tref.cancel()
            self.tref = None
        print('{0} Called when the worker shuts down.'.format(self.IDENT))
            
    def detect(self, worker):
        print('{0} Called when the worker detect deadlock.'.format(self.IDENT))
        for req in worker.state.active_requests:
            if req.time_start and time.time() - req.time_start > self.timeout:
                raise SystemExit()