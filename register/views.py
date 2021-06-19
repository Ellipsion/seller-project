from django.contrib.auth.models import User
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.forms import PasswordChangeForm
from .forms import registerform, update_profile

# Create your views here.
def register(response):
    '''
    Registering user using default django forms.
    '''
    if response.method == "POST":
        form = registerform(response.POST)
        if form.is_valid():
            form.save()
            return redirect("..")
    else:
        form = registerform()
    return render(response, "register/register.html", {'form':form})

def home(response):
    user = response.user
    return render(response, "register/home_page.html", {'user':user})

def userprofile(response):
    username = response.user
    if response.method == 'POST':
        form = update_profile(response.POST, instance=response.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("../../login")
    else:
        form = update_profile()
    return render(response, "register/account.html", {'form':form, 'user': username})


def logout_view(response):
    logout(response)
    return redirect(response, "register/logout_success.html", {})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('../../')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'register/change-password.html', {'form': form})