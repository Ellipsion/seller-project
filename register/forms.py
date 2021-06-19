from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields

class registerform(UserCreationForm):
    username = forms.CharField(max_length=100, required=True, help_text='')
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput,
                                help_text='Minimum 8 characters.<br>Must include an uppercase letter, a lowercase letter and a symbol.',
                                error_messages={'msg':'Must include an uppercase letter, a lowercase letter and a symbol'})
    password2 = forms.CharField(label='Confirm Password',
                                widget=forms.PasswordInput,
                                help_text='Enter the same password as above.',
                                error_messages={'msg':'Make sure you entered the same password as above. Passwords are case sensitive.'})

    class Meta:
        model = User # Changes the user model.(default)
        fields = ["username", "email", "password1", "password2"]


class login(UserCreationForm):
        def __init__(self, *args, **kwargs):
            super(login, self).__init__(*args, **kwargs)
            self.fields['username'].widget.attrs['placeholder'] = 'username'
            self.fields['password '].widget.attrs['placeholder'] = 'password'