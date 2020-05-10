from django.shortcuts import render


# Create your views here.
from home.models import Tutoriais


def home(request):
    return render(request, 'home.html')


def autor(request):
    return render(request, 'autor.html')

def tutoriais(request):
    listaTutoriais= Tutoriais.objects.all()
    context = {
        'tutoriais': listaTutoriais
    }
    return render(request, 'tutoriais.html', context)
