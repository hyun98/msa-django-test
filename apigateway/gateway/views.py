from datetime import datetime
import requests, json

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .tasks import show, posttest, gettest
from config.celery import debug_task
from celery import uuid

class Testview(APIView):
    pass
    # def get(self, request):
        
    #     response = requests.get("http://profile-service:8001/api")
    #     response = json.loads(response.content)
        
    #     ret = show.delay("hello")
    #     print(ret)
        
    #     return Response({
    #         "message": f"{response['message']}"
    #     }, status=status.HTTP_200_OK)
    
    
    # def post(self, request):
    #     username = request.data.get("name")
        
    #     user, created = User.objects.get_or_create(name=username)
        
    #     now = datetime.now()
        
    #     data = {
    #         "user_id": user.pk,
    #         "login_time": now.strftime('%Y-%m-%d %H:%M:%S')
    #     }
        
    #     response = posttest.delay(data)
    #     message = response.get()
    #     print(message)
        
    #     context = {
    #         "message": message
    #     }
    #     return Response(context)


class Gateway(APIView):
    authentication_classes = ()
    permission_classes = ()
    
    def get(self, request, *args, **kwargs):
        print("header : ", request.headers)
        response = gettest.delay()
        message = response.get()
        print(message)
        print(type(message))
        
        print("rabbitmq")
        
        return Response({
            "message": message
        }, status=status.HTTP_200_OK)
        
    def post(self, request, *args, **kwargs):
        
        print("path : ", request.path)
        print("method : ", request.method)
        print("kwargs : ", kwargs)
        print("args : ", args)
        
        username = request.data.get("name")
        
        user, created = User.objects.get_or_create(name=username)
        
        now = datetime.now()
        
        data = {
            "user_id": user.pk,
            "login_time": now.strftime('%Y-%m-%d %H:%M:%S')
        }
        
        response = posttest.delay(data)
        message = response.get()
        print(message)
        
        context = {
            "message": message
        }
        return Response(context)

# {
#     "name": "test1"
# }