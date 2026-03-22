from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={ 
            'class': 'form-control',
           'id': 'birth-date',
            'type': 'date'}),
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username',  'first_name', 'last_name', 'email', 'password1', 'password2', 'birth_date']
        widgets = {
          
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }