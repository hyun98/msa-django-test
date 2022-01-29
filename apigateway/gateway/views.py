from datetime import datetime
import requests, json

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User

class Testview(APIView):
    def get(self, request):
        res = ""
        
        response = requests.get("http://profile-service:8001/api")
        response = json.loads(response.content)
        
        
        return Response({
            "message": f"{response['message']}"
        }, status=status.HTTP_200_OK)
        
    
    
    def post(self, request):
        username = request.data.get("name")
        
        user, created = User.objects.get_or_create(name=username)
        
        now = datetime.now()
        
        data = {
            "user_id": user.pk,
            "login_time": now.strftime('%Y-%m-%d %H:%M:%S')
        }
        
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        response = requests.post("http://profile-service:8001/api/",
                                 data=json.dumps(data), headers=headers)
        
        # print(response.status_code)
        message = json.loads(response.content)["message"]
        return Response(message)
        

# {
#     "name": "test1"
# }