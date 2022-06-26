from dataclasses import fields
from django.forms import ModelForm
from tv.models import Filme

class FilmeForm(ModelForm):
    class Meta:
        model = Filme
        fields = ['titulo', 'genero', 'ano']

