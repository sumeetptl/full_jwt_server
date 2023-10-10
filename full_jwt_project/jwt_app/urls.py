from django.urls import path, include
from jwt_app.views import UserRegisterationView, UserLoginView, UserProfileView, UserChangePassword, SendPasswordResetEmailView, ResetPasswordView

urlpatterns = [
    path('register/',UserRegisterationView.as_view(), name="Registeration" ),
    path('login/',UserLoginView.as_view(), name="Login" ),
    path('profile/',UserProfileView.as_view(), name="Profile"),
    path('change_password/',UserChangePassword.as_view(), name="Change_Password"),
    path('reset_password_email/',SendPasswordResetEmailView.as_view(), name="Send_Email"),
    path('reset_password/<str:uid>/<str:token>/',ResetPasswordView.as_view(), name="Reset Password")
    
]
