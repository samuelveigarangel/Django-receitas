from django.shortcuts import render, get_object_or_404, redirect
from receitas.models import Receita
from django.contrib.auth.models import User


def index(request):
    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    dados = {
        'receitas': receitas
    }

    return render(request, 'receitas/index.html', dados)


def receita(request, receita_id):

    receita = get_object_or_404(Receita, pk=receita_id)

    receita_exibir = {
        'receita': receita
    }

    return render(request, 'receitas/receita.html', receita_exibir)


def buscar(request):

    if 'buscar' in request.GET:
        nome_buscar = " ".join(request.GET['buscar'].split())
        if nome_buscar:
            lista_receitas = Receita.objects.filter(nome_receita__unaccent__icontains=nome_buscar)
        elif nome_buscar == '':
            return redirect('index')
    else:
        lista_receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    dados = {
        'receitas': lista_receitas
    }

    return render(request, 'receitas/buscar.html', dados)


def criar_receita(request):
    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        if 'foto_receita' in request.FILES:
            foto_receita = request.FILES['foto_receita']
        else:
            foto_receita = None
        user = get_object_or_404(User, pk=request.user.id)
        try:
            receita = Receita.objects.create(pessoa=user, nome_receita=nome_receita, ingredientes=ingredientes,
                modo_preparo=modo_preparo, tempo_preparo=tempo_preparo, rendimento=rendimento, categoria=categoria,
                foto_receita=foto_receita, publicada=True)
            receita.save()
        except Exception as e:
            print(e)
        return redirect('dashboard')
    else:
        return render(request, 'receitas/criar_receita.html')


def edita_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita_a_editar = {
        'receita': receita
    }
    return render(request, 'receitas/edita_receita.html', receita_a_editar)


def atualiza_receita(request):
    if request.method == 'POST':
        receita_id = request.POST['receita_id']
        r = Receita.objects.get(pk=receita_id)
        r.nome_receita = request.POST['nome_receita']
        r.ingredientes = request.POST['ingredientes']
        r.modo_preparo = request.POST['modo_preparo']
        r.tempo_preraro = request.POST['tempo_preparo']
        r.rendimento = request.POST['rendimento']
        r.categoria = request.POST['categoria']
        if 'foto_receita' in request.FILES:
            r.foto_receita = request.FILES['foto_receita']
        r.save()
        return redirect('dashboard')


def deleta_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita.delete()
    return redirect('dashboard')