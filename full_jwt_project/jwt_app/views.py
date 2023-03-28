from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from jwt_app.serializers import UserRegistrationSerializer, UserLoginSerializer
from jwt_app.models import User
from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserRegisterationView(APIView):
    def post(self,request,format=None):
        serializer=UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(request.data)
            token = get_tokens_for_user(user=user)
            return Response({"token":token,"msg":"User Registered Succesfully"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self,request,format=None):
        data=request.data
        serializer=UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            email = data.get("email")
            password = data.get("password")
            try:
                user=User.objects.get(email=email)
                token = get_tokens_for_user(user=user)
            except User.DoesNotExist:
                return Response({"msg":"User Doesn't Exist"},status=status.HTTP_400_BAD_REQUEST)
            if user.password == password:
                return Response({"token":token,"msg":"Login Succesful"},status=status.HTTP_200_OK)
            return Response({"msg":"Invalid Password"},status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)