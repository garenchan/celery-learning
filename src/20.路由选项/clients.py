from tasks import app, add


if __name__ == '__main__':
    async_result = add.apply_async((2, 3), queue='priority.high')
    ret = async_result.get()
    print('Result: %s' % ret)


