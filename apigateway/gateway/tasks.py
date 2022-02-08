from __future__ import absolute_import, unicode_literals
import json
import requests
from celery import shared_task


@shared_task
def show(name):
    return f"my name is {name}"

@shared_task
def add(x, y):
    return x + y

@shared_task
def mul(x, y):
    return x * y

@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def gettest():
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    response = requests.get("http://profile-service:8001/api",
                            headers=headers)
    
    response_content = response.content.decode('utf-8')
    message = json.loads(response_content)["message"]
    return message


@shared_task
def posttest(data):
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    response = requests.post("http://profile-service:8001/api/",
                                data=json.dumps(data), headers=headers)
    
    response_content = response.content.decode('utf-8')
    message = json.loads(response_content)["message"]
    return message
