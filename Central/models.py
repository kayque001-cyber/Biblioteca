from django.db import models


class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=150)
    isbn = models.CharField(max_length=20)
    editora = models.CharField(max_length=100)
    ano_publicacao = models.IntegerField()
    categoria = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField(default=1)
    disponiveis = models.PositiveIntegerField(default=1)
    descricao = models.TextField(blank=True)
    capa = models.ImageField(
        upload_to='capas/',
        blank=True,
        null=True,
        verbose_name='Capa do livro',
    )

    def __str__(self):
        return self.titulo