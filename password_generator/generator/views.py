from django.shortcuts import render
from django.http.response import HttpResponse
import random

# Create your views here.

def home(request):

    return render(request, 'generator/home.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    length = request.GET.get('length')

    if length=='Determine the length of the password':
        return render(request, 'generator/error_length.html')
    else:
        length = int(length)
        if request.GET.get('uppercase'):
            characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        if request.GET.get('special'):
            characters.extend(list('!@#$%^&*()_+=-'))
        if request.GET.get('numbers'):
            characters.extend(list('0123456789'))

        thepassword = ''

        for x in range(length):
            thepassword += random.choice(characters )

        return render(request, 'generator/password.html', {'password':thepassword})

def auth(request):

    return render(request, 'generator/index.html')