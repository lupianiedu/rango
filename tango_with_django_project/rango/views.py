from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<p>Rango says hey there world!</p>"
                        "<a href='/rango/about/'>about</a>")

def about(request):
    return HttpResponse("<p>Rango says here is the about page.</p>"
                        " <a href='/rango/'>Index</a>")