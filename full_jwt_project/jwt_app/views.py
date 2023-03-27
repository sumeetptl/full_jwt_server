from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from jwt_app.serializers import UserRegistrationSerializer

class UserRegisterationView(APIView):
    def post(self,request,format=None):
        serializer=UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(request.data)
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
