# Create your tasks here
from __future__ import absolute_import
from celery import Celery
import time
from celery import shared_task

app = Celery('tasks', backend="redis", broker='redis://localhost:6379')

# app = Celery('tasks', backend="amqp", broker='amqp://guest@localhost:5672//')


@app.task
def add(x, y):
    print('hello celery')
    time.sleep(2)
    return x + y



# >>> from core.tasks import add
# >>> result = add.delay(4, 4)
#dir(result)

# celery -A mysite worker -l info --pool=solo --->>> funcionou
# celery -A mysite worker -l info -P threads

# r = redis.Redis(host=settings.REDIS_HOST,
#                 port=settings.REDIS_PORT,
#                 db=settings.REDIS_DB)

# c:/Users/peraz/Documents/Python/celresults/venv/Scripts/activate.bat

# celery --app=projd worker --loglevel=INFO
# celery --app=projd worker --loglevel=INFO --queue=fila1 

# celery -A projd flower

# python manage.py migrate django_celery_results

# python manage.py runserver

# python manage.py shell

# result.state
# result.status