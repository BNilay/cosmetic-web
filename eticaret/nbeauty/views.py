from django.shortcuts import render


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

