import traceback
from tasks import app
from tasks import test_task_time_limit, add

if __name__ == '__main__':
    conf = app.conf
    for option in conf:
        print('%s = %r' % (option, getattr(conf, option, None)))