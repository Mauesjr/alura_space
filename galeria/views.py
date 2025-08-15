from django.shortcuts import render
from galeria.models import Foto



def index(request):
    fotografias = Foto.objects.all()
    return render(request, 'index.html', {'cards': fotografias})

def imagem(request):
    return render(request, 'imagem.html')