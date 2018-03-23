from tasks import app, add


if __name__ == '__main__':
    add.apply_async((2, 3), retry=True, retry_policy={
        'max_retries': 3,
        'interval_start': 0,
        'interval_step': 0.2,
        'interval_max': 0.2,
    })


