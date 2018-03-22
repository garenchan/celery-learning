from tasks import add

if __name__ == '__main__':
    async_result = add.delay(2, 3)
    result = async_result.get(timeout=3)
    print(result)