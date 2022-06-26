from django.shortcuts import render, redirect
from filme.forms import FilmeForm


# Create your views here.

def cadastrar_filme(request):
    data = {}
    data['form'] = FilmeForm()
    return render(request, 'pgn.html', data)

def create(request):
    form = FilmeForm(request.POST or None)
    if form.is_valid():
        form.save
        return redirect('home')