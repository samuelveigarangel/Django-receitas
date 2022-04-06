from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('criar/receita', views.criar_receita, name='criar_receita'),
    path('logout', views.logout, name='logout'),
    path('deleta/<int:receita_id>', views.deleta_receita, name='deleta_receita'),
    path('edita/<int:receita_id>', views.edita_receita, name='edita_receita'),
    path('atualiza_receita', views.atualiza_receita, name='atualiza_receita'),
]