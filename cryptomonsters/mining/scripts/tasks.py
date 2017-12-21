from celery import Celery
import time


# app.conf.broker_url = 'redis://localhost:6379/0'

app = Celery('tasks',
             broker='redis://localhost',
             # backend='db+postgresql://localhost:5432/async_tasks'
             backend='redis://localhost'
             )


@app.task(name='tasks.rev')
def rev(string):
    time.sleep(10)
    a = string[::-1]
    return a


def call(string):
    return rev.delay(string)