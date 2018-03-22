from tasks import add, sub

if __name__ == '__main__':
    try:
        async_result = add.delay(2)
    except TypeError as ex:
        print(ex)
    
    async_result = sub.delay(2)
