from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),

    path(
        'livros/',
        views.lista_livros,
        name='lista_livros'
    ),

    path(
        'livros/<int:livro_id>/',
        views.detalhe_livro,
        name='detalhe_livro'
    ),
]