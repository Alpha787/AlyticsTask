from dashboard.models import Dashboard
from celery import Task
from time import sleep
from AlyticsDashboard.celery import app

@app.task
def hello_world():
    sleep(10) # задержка 10 секунд
    print('Hello World')


