from django.shortcuts import render
from filme.forms import Filme

# Create your views here.

def home(request):
    return render(request, 'index.html')

