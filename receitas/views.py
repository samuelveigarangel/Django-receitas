from django.shortcuts import render, get_object_or_404
from .models import Receita

def index(request):
    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    dados = {
        'receitas': receitas
    }

    return render(request, 'index.html', dados)

def receita(request, receita_id):

    receita = get_object_or_404(Receita, pk=receita_id)

    receita_exibir = {
        'receita': receita
    }

    return render(request, 'receita.html', receita_exibir)

def buscar(request):

    if 'buscar' in request.GET:
        nome_buscar = request.GET['buscar']
        if nome_buscar:
            lista_receitas = lista_receitas = Receita.objects.filter(nome_receita__unaccent__icontains=nome_buscar)
    else:
        lista_receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    dados = {
        'receitas': lista_receitas
    }

    return render(request, 'buscar.html', dados)