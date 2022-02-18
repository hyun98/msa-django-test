from datetime import datetime
import requests, json

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Profile

class Testview(APIView):
    authentication_classes = ()
    permission_classes = ()
    
    def get(self, request):
        print("origin : ", request.path)
        
        data = {
            "data": [
                {
                    "name": "a"
                },
                {
                    "name": "b"
                }
            ]
        }
        # test = {}
        
        return Response(data, status=status.HTTP_200_OK)
    
    
    def post(self, request):
        user_id = request.data["user_id"]
        login_time = request.data["login_time"]
        print(user_id, login_time)
        profile, Created = Profile.objects.get_or_create(user_id=user_id)
        print(profile)
        profile.last_login = datetime.strptime(login_time, '%Y-%m-%d %H:%M:%S')
        profile.save()
        
        return Response({
            "message": "Login successful"
        }, status=status.HTTP_200_OK)

# class testa(APIView):
#     authentication_classes = ()
#     permission_classes = ()
    
#     def post(self, request, *args, **kwargs):
        
#         print("testa redirect : ", request.path)
        
#         return Response({
#             "message": "tesa called"
#         }, status=status.HTTP_200_OK)
    
#     def post(self, request):
#         user_id = request.data["user_id"]
#         login_time = request.data["login_time"]
#         print(user_id, login_time)
#         profile, Created = Profile.objects.get_or_create(user_id=user_id)
#         print(profile)
#         profile.last_login = datetime.strptime(login_time, '%Y-%m-%d %H:%M:%S')
#         profile.save()
        
#         return Response({
#             "message": "Login successful"
#         }, status=status.HTTP_200_OK)


# class Gateway(APIView):
#     authentication_classes = ()
#     permission_classes = ()
    
#     def get(self, request, *args, **kwargs):
        
#         return Response({
#             "message": "GET gateway called"
#         }, status=status.HTTP_200_OK)
        
#     def post(self, request, *args, **kwargs):
        
#         print("path : ", request.path)
#         print("method : ", request.method)
#         print("kwargs : ", kwargs)
#         print("args : ", args)
        
#         return Response({
#             "message": f"POST gateway called "
#         }, status=status.HTTP_200_OK)
        
# {
#     "name": "test1"
# }