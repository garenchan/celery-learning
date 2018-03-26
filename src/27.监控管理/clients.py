from tasks import app, add, log


if __name__ == '__main__':
    log.delay('DEBUG', 'test routes')
    add.delay(1, 2)