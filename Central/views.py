from django.contrib import messages
from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect, render

from .forms import LivroForm
from .models import Livro, Emprestimo


def inicio(request):
    total_livros = Livro.objects.count()

    total_exemplares = Livro.objects.aggregate(
        total=Sum('quantidade')
    )['total'] or 0

    total_disponiveis = Livro.objects.aggregate(
        total=Sum('disponiveis')
    )['total'] or 0

    return render(request, 'pages/base.html', {
        'total_livros': total_livros,
        'total_exemplares': total_exemplares,
        'total_disponiveis': total_disponiveis,
    })


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


def detalhe_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)

    return render(request, 'pages/detalhe_livro.html', {
        'livro': livro,
    })


def criar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'Livro cadastrado com sucesso!')
            return redirect('lista_livros')
    else:
        form = LivroForm()

    return render(request, 'pages/livro_form.html', {
        'form': form,
        'titulo_pagina': 'Cadastrar livro',
    })


def editar_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)

    if request.method == 'POST':
        form = LivroForm(
            request.POST,
            request.FILES,
            instance=livro
        )

        if form.is_valid():
            form.save()
            messages.success(request, 'Livro atualizado com sucesso!')
            return redirect(
                'detalhe_livro',
                livro_id=livro.id
            )
    else:
        form = LivroForm(instance=livro)

    return render(request, 'pages/livro_form.html', {
        'form': form,
        'titulo_pagina': 'Editar livro',
        'livro': livro,
    })


def excluir_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)

    if request.method == 'POST':
        livro.delete()
        messages.success(request, 'Livro excluído com sucesso!')
        return redirect('lista_livros')

    return render(request, 'pages/livro_confirm_delete.html', {
        'livro': livro,
    })


def lista_emprestimos(request):
    emprestimos = Emprestimo.objects.all().order_by(
        '-data_emprestimo'
    )

    return render(
        request,
        'pages/emprestimos.html',
        {'emprestimos': emprestimos}
    )
