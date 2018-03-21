import traceback
from tasks import add, raise_error

if __name__ == '__main__':
    # do task in sync mode
    sync = add(1, 2)
    print('sync: %s' % sync)
    
    
    # do task in async mode
    # if we not care about result, it's ok
    add.delay(1, 2)
    # if we want to get the result now
    # first we need to configure the backend where to store result.
    async_result = add.delay(1, 2)
    # we can use ready() method to judge whether result is returned
    ready = async_result.ready()
    print('result ready: %s' % ready)
    # set timeout to wait result
    result = async_result.get(timeout=1)
    print('async result: %s' % result)
    
    
    # Test raise exception
    async_result = raise_error.delay()
    try:
        result = async_result.get(timeout=1)
    except Exception as ex:
        traceback.print_exc()
    # not raise
    async_result = raise_error.delay()
    result = async_result.get(propagate=False)
    print('not raise error: %s' % result)