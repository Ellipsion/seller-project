from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
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

class update_profile(forms.ModelForm):
    Name = forms.CharField(max_length=100, required=True)
    Email_id = forms.EmailField(required=True)
    Mobile = forms.IntegerField(required=True)
    Address = forms.CharField(required=True)
    Landmark = forms.CharField(required=True)
    State = forms.CharField(max_length=20, required=True)
    Pin_code = forms.IntegerField(max_value=999999,min_value=000000, required=True)
    
    class Meta:
        model = User
        fields = ["Name", "Email_id", "Mobile", "Address", "Landmark", "State", "Pin_code"]



class login(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(login, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'username'
        self.fields['password '].widget.attrs['placeholder'] = 'password'
