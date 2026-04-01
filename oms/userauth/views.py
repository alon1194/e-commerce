from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView 
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .forms import CustomUserCreationForm
from .models import Profile

class CustomLoginView(LoginView):
    template_name = "auth/login.html"

    def get_success_url(self):
        return reverse_lazy('shop:home')



class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    redirect_authenticated_user = True
    template_name = 'auth/register.html'
    success_url = reverse_lazy('userauth:login')  

    def form_valid(self, form):
     
        response = super().form_valid(form)
        birth_date = form.cleaned_data['birth_date']
        Profile.objects.create(user=self.object, birth_date=birth_date)
        return response

class CustomPasswordResetView(PasswordResetView):
    template_name = 'auth/password_reset.html'   # your template
    email_template_name = 'auth/password_reset_email.html'  # email template
   
    success_url = reverse_lazy('auth/password_reset_done')
    
from django.contrib.auth.views import PasswordResetConfirmView

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'auth/password_reset_confirm.html'  # form to set new password
    success_url = reverse_lazy('login')  # redirect after password is set