from receitas.models import Receita
from django.shortcuts import redirect, render

def busca(request):

    if 'buscar' in request.GET:
        nome_buscar = " ".join(request.GET['buscar'].split())
        if nome_buscar:
            lista_receitas = Receita.objects.filter(nome_receita__unaccent__icontains=nome_buscar)
    else:
        lista_receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    dados = {
        'receitas': lista_receitas
    }

    return render(request, 'receitas/buscar.html', dados)