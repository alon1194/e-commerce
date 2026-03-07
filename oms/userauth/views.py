from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = "auth/login.html"
    