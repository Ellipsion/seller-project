from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .forms import registerform

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

def loginsuccess(response):
    '''
    User login page.
    '''
    return render(response, "register/loginsuccess.html", {})

def logoutsuccess(response):
    return render(response, "register/logoutsuccess.html", {})

def home(response):
    return render(response, "register/home_page.html", {})