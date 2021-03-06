from django.urls import path

from apps.receitas.views import *

urlpatterns = [
    path('', index, name='index'),
    path('<int:receita_id>', receita, name='receita'),
    path('busca', buscar, name='buscar'),
    path('criar/receita', criar_receita, name='criar_receita'),
    path('deleta/<int:receita_id>', deleta_receita, name='deleta_receita'),
    path('edita/<int:receita_id>', edita_receita, name='edita_receita'),
    path('atualiza_receita', atualiza_receita, name='atualiza_receita'),
]