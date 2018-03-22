from celery import states

from tasks import test_task_handler

if __name__ == '__main__':
    commands = [states.SUCCESS, states.FAILURE, states.RETRY]
    for command in commands:
        test_task_handler.delay(command)
    

