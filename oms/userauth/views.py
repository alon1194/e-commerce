from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomRegistrationForm

class CustomRegisterView(CreateView):
    template_name = "auth/register.html"
    redirect_authenticated_user = True
    form_class = CustomRegistrationForm
    success_url = reverse_lazy("userauth:login")