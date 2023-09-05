from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput())    
    # first_name = forms.CharField(max_length=100, 
    #                              widget=forms.TextInput())
    # last_name = forms.CharField(max_length=100, 
    #                             widget=forms.TextInput())
    # email = forms.EmailField(max_length=100, 
    #                          required=True, 
    #                          widget=forms.EmailInput())
    password1 = forms.CharField(max_length=50,
                                min_length=6,
                                required=True,
                                widget=forms.PasswordInput())    
    password2 = forms.CharField(max_length=50,
                                min_length=6,
                                required=True,
                                widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 
                  'password1', 'password2']

class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']

