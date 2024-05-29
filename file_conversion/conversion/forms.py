from django import forms
from django.forms import ModelForm
from .models import User

# Create a account form
class UserForm(ModelForm): 
    class Meta:
        model = User
        fields = ('username', 'password')
        labels = {
            'username': '',
            'password': ''
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'password': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
        }

