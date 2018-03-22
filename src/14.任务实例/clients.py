from tasks import app, register_user
import time 

if __name__ == '__main__':
    users = {'xiaoming': 'admin123', 
             'lily': 'admin123',
             'garen': 'admin123'}
    for username, password in users.items():
        async_result = register_user.delay(username, password)
    result = async_result.get(timeout=3)
    print(result)
    assert result == users

