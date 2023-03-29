from django.urls import path, include
from jwt_app.views import UserRegisterationView, UserLoginView, UserProfileView, UserChangePassword

urlpatterns = [
    path('register/',UserRegisterationView.as_view(), name="Registeration" ),
    path('login/',UserLoginView.as_view(), name="Login" ),
    path('profile/',UserProfileView.as_view(), name="Profile"),
    path('change_password/',UserChangePassword.as_view(), name="Change_password"),
    

]
