from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')


def autor(request):
    return render(request, 'autor.html')

def tutorial(request):
    listaTutorial = tutorial.objects.all()
    context = {
        'tutorial': listaTutorial
    }
    return render(request, 'tutorial.html', context)
