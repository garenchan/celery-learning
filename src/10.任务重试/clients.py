from tasks import retry_without_limit, retry_with_custome_delay, \
                  retry_with_max_times, retry_with_know_exceptions, \
                  retry_with_exp_backoff

if __name__ == '__main__':
    tasks = [retry_without_limit, retry_with_custome_delay, retry_with_max_times, 
                retry_with_know_exceptions, retry_with_exp_backoff]
    async_results = []
    for task in tasks:
        async_results.append(task.delay())

