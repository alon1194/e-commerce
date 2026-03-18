from django.urls import path 
from .views import CustomLoginView,  RegisterView; 



app_name = "userauth"

urlpatterns = [
   path("", CustomLoginView.as_view(), name="login"),
   path("Register/", RegisterView.as_view(), name = "Register")
]