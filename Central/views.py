from django.shortcuts import render
from .models import Livro


def inicio(request):
    return render(request, 'pages/base.html')


def lista_livros(request):
    livros = Livro.objects.all()

    return render(request, 'pages/livros.html', {
        'livros': livros
    })