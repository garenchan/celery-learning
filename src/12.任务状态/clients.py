from tasks import track_task_state_with_custom, track_task_state
import time 

if __name__ == '__main__':
    tasks = [track_task_state, track_task_state_with_custom]
    for task in tasks:
        async_result = task.delay()
        print('Current task name: {0}, id: {1}'.format(task.name, async_result.task_id))
        current_state = None
        while not async_result.ready():
            if current_state != async_result.state:
                current_state = async_result.state
                print('Current state: %s' % current_state)
            time.sleep(5)
        print('Current state: %s\n' % async_result.state)
    

