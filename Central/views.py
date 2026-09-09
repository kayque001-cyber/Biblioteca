from django.shortcuts import render
from django import forms
from .models import Livro

def index(request):
    return render(request, 'pages/index.html')

def livros(request):
    lista_livros = Livro.objects.all()
    return render(request, 'pages/livros.html', {'livros': lista_livros})

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'editora' , 'ano_publicacao', 'categoria', ]
    
    