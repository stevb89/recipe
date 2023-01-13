import re
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "recipes/home.html")

def hello(request, name):
    return render(
        request,
        'recipes/hello.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

def about(request):
    return render(request, "recipes/about.html")

def contact(request):
    return render(request, "recipes/contact.html")