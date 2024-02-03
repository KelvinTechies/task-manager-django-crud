from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

from .models import Record

class createUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    class Meta:
        username:forms.CharField(widget=TextInput())
        password=forms.CharField(widget=PasswordInput())



class CreateTaskForm(forms.ModelForm):
    class Meta:
        model=Record
        fields=['first_name', 'last_name', 'task', 'description']



class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model=Record
        fields=['first_name', 'last_name', 'task', 'description']