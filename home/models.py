from django.db import models


# Create your models here.
class Autor(models.Model):
    nome = models.CharField('nome', max_length=100)
    email = models.EmailField()
    telefone = models.CharField('telefone',max_length=15)


class Tutoriais(models.Model):
    nome = models.CharField('nome', max_length=150)
    titulo = models.CharField('titulo', max_length=150)
    data = models.DateTimeField('data')
    imagem = models.ImageField(upload_to='media')
    conteudo = models.TextField('conteudo')
    autor = models.ForeignKey(Autor,  models.SET_NULL,blank=True,null=True,)
