from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def Home(request):
    return render(request, 'generator/home.html')


def Password(request):
    password = ''
    chars = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length'))

    if(request.GET.get('uppercase')):
        chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if(request.GET.get('specialcase')):
        chars.extend(list('!@#$%^&*'))

    if(request.GET.get('numbers')):
        chars.extend(list('1234567890'))

    for i in range(length):
        password += random.choice(chars)
    return render(request, 'generator/password.html', {'passwordtext': password})


def About(request):
    return render(request, 'generator/about.html')
