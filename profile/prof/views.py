import requests, json

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class Testview(APIView):
    def get(self, request):
        
        return Response({
            "message": "call profile's Testview"
        }, status=status.HTTP_200_OK)

