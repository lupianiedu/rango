from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'rango/index.html', context_dict)


def about(request):
    return render(request, 'rango/about.html')