import json

from celery import signature

from tasks import add


if __name__ == '__main__':
    # shorcut: add.s(2, 2)
    # or: signature('tasks.add', args=(2, 2), countdown=10)
    sig = add.signature((2, 2), countdown=3)
    print(sig, json.dumps(sig))
    
    # call local
    ret = sig()
    print('Call local: %s' % ret)
    
    # call remote
    # NOTE: ~sig is equal to sig.delay().get()
    async_ret = sig.delay()
    ret = async_ret.get()
    print('Call remote: %s' % ret)
    
    # paitial
    partial = add.s(2)
    async_ret = partial.delay(3)
    ret = async_ret.get()
    print('Partial: %s' % ret)
    
    async_ret = add.apply_async((2, 2), link=add.signature((3, 3), immutable=True))
    ret = async_ret.get()
    print('Use signature in task link: %s' % ret)


