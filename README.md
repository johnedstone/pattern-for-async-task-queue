### pattern-for-async-task-queue

Based on http://matthewminer.com/2015/02/21/pattern-for-async-task-queue-results.html and https://github.com/mminer/blog-code/tree/master/pattern-for-async-task-queue-results

Writing docker-compose.yml as was done [earlier](https://github.com/johnedstone/docker-django-celery.git)

Notes:
  - How to run rabbitmq from the command line: ```docker run --publish=5672:5672 --detach rabbitmq:3.4```
  - How to use flask cli for debugging, although this only listens on 127.0.0.1 ```flask -a server --debug run```
