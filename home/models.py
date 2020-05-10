from django.db import models


# Create your models here.
class Autor(models.Model):
    nome = models.CharField('nome', max_length=100)
    email = models.DecimalField('email', decimal_places=2, max_digits=7)
    telefone = models.IntegerField('telefone')


class Tutoriais(models.Model):
    nome = models.CharField('nome', max_length=50)
    titulo = models.CharField('titulo', max_length=50)
    data = models.CharField('data', max_length=21)
    imagem = models.CharField('imagem', max_length=150)
    conteudo = models.CharField('conteudo', max_length=800)
    autor = models.CharField('autor', max_length=50)
