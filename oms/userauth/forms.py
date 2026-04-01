from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    birth_date = forms.DateField(
        widget=forms.DateInput(
            attrs={ 
                'class': 'form-control',
                'id': 'birth-date',
                'type': 'date'
            }
        ),
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username',  'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # override the password fields properly
        self.fields['password1'].widget.attrs.update({'class': 'form-control w-100'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control w-100'})