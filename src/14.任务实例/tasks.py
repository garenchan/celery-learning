from celery import Celery
from celery import Task
from celery import states

app = Celery('tasks',
             backend='amqp://agent:agent@172.18.231.134:5672',
             broker='amqp://agent:agent@172.18.231.134:5672')
             
             
class RegisterTask(Task):
    _db = None
    
    def __init__(self, *args, **kwargs):
        super(RegisterTask, self).__init__(*args, **kwargs)
        print('{0} object init'.format(RegisterTask.__name__))
    
    @property
    def db(self):
        if self._db is None:
            self._db = {}
        return self._db
    
    def register(self, username, password):
        self.db[username] = password
    
    def dump(self):
        return self.db


# The task only be instantiated once per process, it won't be instantiated for event request!
# So it will keep state between requests. We can cache something useful for example db connection!
@app.task(base=RegisterTask)
def register_user(username, password):
    register_user.register(username, password)
    return register_user.dump()
