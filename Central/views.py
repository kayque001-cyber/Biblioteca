from django.shortcuts import render
from .models import Livro


def inicio(request):
    return render(request, 'pages/base.html')


def lista_livros(request):
    livros = Livro.objects.all()

    busca = request.GET.get('busca')

    if busca:
        livros = livros.filter(
            titulo__icontains=busca
        ) | livros.filter(
            autor__icontains=busca
        ) | livros.filter(
            categoria__icontains=busca
        )

    return render(request, 'pages/livros.html', {
        'livros': livros,
        'busca': busca,
    })