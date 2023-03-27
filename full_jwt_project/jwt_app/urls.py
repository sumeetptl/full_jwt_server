from django.urls import path, include
from jwt_app.views import UserRegisterationView

urlpatterns = [
    path('register/',UserRegisterationView.as_view(), name="Registeration" ),
]
