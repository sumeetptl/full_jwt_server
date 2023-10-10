from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from jwt_app.serializers import UserProfileSerializer, UserRegistrationSerializer,UserLoginSerializer, ChangePasswordSerializer, SendPasswordResetEmailSerializer, ResetPasswordSerializer
from jwt_app.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from jwt_app.renderers import UserRenderer

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserRegisterationView(APIView):
    renderer_classes=[UserRenderer]
    def post(self,request,format=None):
        serializer=UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(request.data)
            token = get_tokens_for_user(user=user)
            return Response({"token":token,"msg":"User Registered Succesfully"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    renderer_classes=[UserRenderer]
    def post(self,request,format=None):
        serializer=UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email=serializer.data.get('email')
            password=serializer.data.get('password')
            try:
                user=User.objects.get(email=email,password=password)
                token=get_tokens_for_user(user) 
                return Response({"token":token,"msg":"User Found"},status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({"msg":"User Doesn't Exist"},status=status.HTTP_200_OK)
        else:
                #serializer use nahi kar rahe isliye custom handle karna pad raha hai..warna as above handle ho jata
            return Response({'errors':{'non_field_errors':["Email or password is not valid"]}},status.HTTP_404_NOT_FOUND)
        # return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
    
class UserProfileView(APIView):
    renderer_classes=[UserRenderer]
    permission_classes=[IsAuthenticated]
    def get(self,request,format=None):
        print("Request",request.user)
        serializer= UserProfileSerializer(request.user)
        return Response(serializer.data,status=status.HTTP_200_OK)      

class UserChangePassword(APIView):
    renderer_classes=[UserRenderer]
    permission_classes=[IsAuthenticated]
    def post(self,request,format=None):
        serializer = ChangePasswordSerializer(data=request.data,context={'user':request.user})
        if serializer.is_valid(raise_exception=True):
            return Response({"msg":"Password Changed Succesfully"},status=status.HTTP_200_OK)    
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST) 
    
class SendPasswordResetEmailView(APIView):
    renderer_classes=[UserRenderer]
    def post(self,request,format=None):
        serializer= SendPasswordResetEmailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({"msg":"Password Reset Email Sent Succesfully"},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class ResetPasswordView(APIView):
    renderer_classes=[UserRenderer]
    def post(self, request, uid, token, format=None):
        serializer = ResetPasswordSerializer(data=request.data,context={'uid' : uid, 'token': token})
        if serializer.is_valid(raise_exception=True):
            return Response({"msg":"Password Reset Succesfully"},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    
    