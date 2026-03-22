from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView 
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .forms import CustomUserCreationForm
from .models import Profile

class CustomLoginView(LoginView):
    template_name = "auth/login.html"



class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('auth/login')  # redirect after successful registration

    def form_valid(self, form):
        # Save the user first
        response = super().form_valid(form)
        # Save birth_date in Profile
        birth_date = form.cleaned_data['birth_date']
        Profile.objects.create(user=self.object, birth_date=birth_date)
        return response