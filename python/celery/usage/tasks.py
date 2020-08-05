import time
import random
from celery import Celery

app = Celery("tasks", broker="amqp://localhost", backend="rpc://")


@app.task
def add(x, y):
    time.sleep(random.randrange(1, 6) / 10)
    return x + y


@app.task
def tsum(results):
    return sum(results)
