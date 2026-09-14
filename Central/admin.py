from django.contrib import admin
from .models import Livro, Aluno, Emprestimo


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = (
        'titulo',
        'autor',
        'categoria',
        'ano_publicacao',
        'quantidade',
        'disponiveis',
    )

    search_fields = (
        'titulo',
        'autor',
        'isbn',
    )

    list_filter = (
        'categoria',
        'ano_publicacao',
    )



@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'matricula',
        'email',
        'turma',
        'data_cadastro',
    )

    search_fields = (
        'nome',
        'matricula',
        'email',
    )

    list_filter = (
        'turma',
        'data_cadastro',
    )




@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = (
        'aluno',
        'livro',
        'data_emprestimo',
        'data_devolucao_prevista',
        'data_devolucao',
        'status',
    )

    search_fields = (
        'aluno__nome',
        'aluno__matricula',
        'livro__titulo',
    )

    list_filter = (
        'status',
        'data_emprestimo',
        'data_devolucao_prevista',
    )