from tasks import track_states
import time

def on_raw_message(body):
    print('[{0}] {1}'.format(time.time(), body))

if __name__ == '__main__':
    async_result = track_states.delay(2, 3)
    result = async_result.get(on_message=on_raw_message, propagate=False)
    print('Result: %s' % result)

