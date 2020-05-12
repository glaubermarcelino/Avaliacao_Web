from django.shortcuts import render


# Create your views here.
from home.models import Tutoriais,Autor


def index(request):
    return render(request, 'home.html')


def autor(request):
    listaAutores = Autor.objects.all()
    context = {
        'autores': listaAutores
    }
    return render(request, 'autor.html', context)

def tutoriais(request):
    listaTutoriais= Tutoriais.objects.all()
    context = {
        'tutoriais': listaTutoriais
    }
    return render(request, 'tutoriais.html', context)
