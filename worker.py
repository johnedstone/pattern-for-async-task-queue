# worker.py
import time
from celery import Celery, Task
# This must be from docker-compose.yml
from config import NOTIFIER_HOST, NOTIFIER_PORT, RABBITMQ_HOST, RABBITMQ_PORT

import requests

class NotifierTask(Task):
    """Task that sends notification on completion."""
    abstract = True

    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        url = 'http://{}:{}/notify'.format(NOTIFIER_HOST, NOTIFIER_PORT)
        # url = 'http://localhost:3000/notify'
        data = {'clientid': kwargs['clientid'], 'result': retval}
        requests.post(url, data=data)
        

# broker = 'amqp://localhost:5672'
broker = 'amqp://{}:{}'.format(RABBITMQ_HOST, RABBITMQ_PORT)
app = Celery(__name__, broker=broker)

@app.task(base=NotifierTask)
def mytask(clientid=None):
     """Simulates some slow computation."""
     time.sleep(10)
     return 42

# vim: set ai sw=4 ts=4 et sts=4
