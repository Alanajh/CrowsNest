from django import forms
from django.forms import ModelForm
from .models import User
from .models import Transform

# Account form
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

# Excel data conversion form
class InputForm(ModelForm):
    class Meta:
        model = Transform
        fields = ('file', 'columns', 'rows')
        widgets = {
            'file': forms.FileInput()
        }