"""
1-
from django.http import HttpResponse
def home(request):
    return HttpResponse('Hallo world')

"""
from django.shortcuts import render
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')
