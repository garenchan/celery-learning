from tasks import app
from snapshot.mycam import DumpCam


def main(app, freq=1.0):
    state = app.events.State()
    
    # process worker-online event
    def worker_online_handler(event):
        state.event(event)
        worker = state.workers.get(event['hostname'])
        print('Worker [{0}] ONLINE at {1}'.format(worker.hostname, worker.timestamp))
        
    with app.connection() as connection:
        recv = app.events.Receiver(connection, handlers={
                    'worker-online': worker_online_handler,
                    '*': state.event
        })
        with DumpCam(state, freq=freq):
            recv.capture(limit=None, timeout=None, wakeup=True)


if __name__ == '__main__':
    main(app)