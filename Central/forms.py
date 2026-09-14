from django import forms

from .models import Livro, Aluno


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro

        fields = [
            'titulo',
            'autor',
            'isbn',
            'editora',
            'ano_publicacao',
            'categoria',
            'quantidade',
            'disponiveis',
            'descricao',
            'capa',
        ]

        labels = {
            'titulo': 'Título',
            'autor': 'Autor',
            'isbn': 'ISBN',
            'editora': 'Editora',
            'ano_publicacao': 'Ano de publicação',
            'categoria': 'Categoria',
            'quantidade': 'Quantidade total',
            'disponiveis': 'Exemplares disponíveis',
            'descricao': 'Descrição',
            'capa': 'Capa do livro',
        }

        widgets = {
            'titulo': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'autor': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'isbn': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'editora': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'ano_publicacao': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),

            'categoria': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'quantidade': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'min': 0
                }
            ),

            'disponiveis': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'min': 0
                }
            ),

            'descricao': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4
                }
            ),

            'capa': forms.ClearableFileInput(
                attrs={'class': 'form-control'}
            ),
        }

    def clean(self):
        cleaned_data = super().clean()

        quantidade = cleaned_data.get('quantidade')
        disponiveis = cleaned_data.get('disponiveis')

        if quantidade is not None and disponiveis is not None:
            if disponiveis > quantidade:
                self.add_error(
                    'disponiveis',
                    'A quantidade de disponíveis não pode ser maior '
                    'que a quantidade total de exemplares.'
                )

        return cleaned_data


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno

        fields = [
            'nome',
            'matricula',
            'email',
            'turma',
        ]

        labels = {
            'nome': 'Nome completo',
            'matricula': 'Matrícula',
            'email': 'E-mail',
            'turma': 'Turma',
        }

        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite o nome completo'
                }
            ),

            'matricula': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite a matrícula'
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite o e-mail'
                }
            ),

            'turma': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite a turma'
                }
            ),
        }