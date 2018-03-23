from tasks import my_sum, my_echo, my_add, my_div, error_handler

if __name__ == '__main__':
    myList = range(50)
    # delay(*args, **kwargs): Shortcut to send a task message, but doesn’t support execution options.
    async_result = my_sum.delay(*myList, name='lily', password='admin', action='login')
    result = async_result.get(timeout=3)
    print('{0}\'s sum is {1}'.format(myList, result))
    
    # apply_async(args[, kwargs[, …]]): Sends a task message.
    async_result = my_echo.apply_async(args=tuple(range(10)), kwargs={'name': 'lily', 'password': 'admin'})
    result = async_result.get(timeout=3)
    print('echo: {0}'.format(result))
    
    # use link option
    async_result = my_add.apply_async(args=(2, 3), link=[my_add.s(16)])
    result = async_result.get(timeout=5)
    print('add: {0}'.format(async_result.result))
    # It's strange: we can only get the first task's result, rather than the final result
    # assert result == (2 + 3 + 16)
    
    # use errback
    async_result = my_div.apply_async(args=(1, 0), link_error=[error_handler.s()])

