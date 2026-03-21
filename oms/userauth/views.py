from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView 
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomLoginView(LoginView):
    template_name = "auth/login.html"

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "auth/Register.html"
    