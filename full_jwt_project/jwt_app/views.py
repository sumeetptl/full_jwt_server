from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class UserRegisterationView(APIView):
    def post(self,request,format=None):
        return Response(data={'msg':"User Registered Succesfully"},status=status.HTTP_201_CREATED)
