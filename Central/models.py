from django.db import models
from django.core.exceptions import ValidationError


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


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    turma = models.CharField(max_length=50)
    data_cadastro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome



class Emprestimo(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    data_emprestimo = models.DateField(auto_now_add=True)
    data_devolucao_prevista = models.DateField()
    data_devolucao = models.DateField(null=True, blank=True)

    status = models.CharField(
        max_length=20,
        choices=[
            ('Emprestado', 'emprestado'),
            ('Devolvido', 'devolvido'),
        ],
        default='Emprestado'
    )

    def save(self, *args, **kwargs):
        if self.pk:
            emprestimo_anterior = Emprestimo.objects.get(pk=self.pk)

            if (
                emprestimo_anterior.status == 'Emprestado'
                and self.status == 'Devolvido'
            ):
                self.livro.disponiveis += 1
                self.livro.save()

        else:
            if self.status == 'Emprestado':
                self.livro.disponiveis -= 1
                self.livro.save()

        super().save(*args, **kwargs)

    def clean(self):
        if (
            self.status == 'Emprestado'
            and self.livro_id
            and self.livro.disponiveis <= 0
        ):
            raise ValidationError({
                'livro': 'Este livro não possui exemplares disponíveis.'
            })

    def __str__(self):
        return f'{self.aluno} - {self.livro}'