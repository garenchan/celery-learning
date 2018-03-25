from tasks import app, add, log


if __name__ == '__main__':
    log.apply_async(('DEBUG', 'test routes'), exchange='logs')
    add.delay(1, 2)