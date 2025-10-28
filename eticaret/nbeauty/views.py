from django.shortcuts import render


def routines(request):
    return render(request,'nbeauty/routines.html')


def home(request):
    return render(request,'nbeauty/home.html')