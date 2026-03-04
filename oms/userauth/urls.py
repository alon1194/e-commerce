from django.urls import path 
from .views import CustomRegisterView

app_name = "userauth"

urlpatterns = [
    path("register/", CustomRegisterView.as_view(), name="register"),
]