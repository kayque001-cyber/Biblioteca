from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect, render

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


def excluir_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)

    if request.method == 'POST':
        livro.delete()
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