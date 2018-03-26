from tasks import app, add

# after use auth task_serializer, the task message's body will be encrypted
# and the content_type in the header will be 'application/data'

if __name__ == '__main__':
    add.delay(1, 2)