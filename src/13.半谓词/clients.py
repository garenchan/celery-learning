from tasks import div_ignore_zero, div_reject_zero, div_retry
import time 

if __name__ == '__main__':
    tasks = [div_ignore_zero, div_reject_zero]
    async_results = {}
    for task in tasks:
        print(task.name)
        async_results[task.name] = task.delay(1, 0)
    print('poll')
    while async_results:
        for name, result in async_results.copy().items():
            if result.ready():
                print('Task id: {0}, state: {1}'.format(name, result.state))
                async_results.pop(name)
        time.sleep(3)

