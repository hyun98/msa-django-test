import requests, json

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class Testview(APIView):
    def get(self, request):
        res = ""
        
        response = requests.get("http://profile-service:8001/api")
        response = json.loads(response.content)
        
        return Response({
            "message": f"{response['message']}"
        }, status=status.HTTP_200_OK)

