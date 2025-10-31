from django.shortcuts import render , redirect
from . import models
from django.urls import reverse , reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

def routines(request):
    return render(request,'nbeauty/routines.html')


def home(request):
    return render(request,'nbeauty/home.html')


def cleanser(request):
    return render(request,'nbeauty/cleanser.html')

def moisturizer(request):
    return render(request,'nbeauty/moisturizer.html')

def serum(request):
    return render(request,'nbeauty/serum.html')

def toner(request):
    return render(request,'nbeauty/toner.html')

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")  # kayıt sonrası login sayfasına
