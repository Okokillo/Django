from django.db import models

# Create your models here.

class Filme(models.Model):
    titulo = models.CharField(max_length=150)
    genero = models.CharField(max_length=150)
    ano = models.IntegerField()