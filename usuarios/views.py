from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages

from receitas.models import Receita


def cadastro(request):
    if request.method == 'POST':
        nome = " ".join(request.POST['nome'].split())
        email = request.POST['email']
        senha1 = request.POST['password']
        senha2 = request.POST['password2']
        if not nome:
            messages.error(request, 'Nome vazio. Tente novamente!')
            return redirect('cadastro')
        if verifica_senha(senha1, senha2):
            messages.error(request, 'Senhas Incompatíveis. Tente novamente!')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'E-mail já existe. Tente outro e-mail!')
            return redirect('cadastro')
        if User.objects.filter(username=nome).exists():
            messages.error(request, 'Usuário já cadastrado')
            return redirect('cadastro')
        try:
            user = User.objects.create_user(username=nome, email=email, password=senha)
            user.save()
        except Exception as e:
            messages.error(request, 'Erro no cadastro. Tente novamente!')
            print(e)
            return redirect('cadastro')
        messages.success(request, 'Cadastro realizado com sucesso!')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha1 = request.POST['senha']
        if campo_vazio(email) or campo_vazio(senha1):
            messages.error(request, 'Login inválido')
            return redirect('login')
        if User.objects.filter(email=email).exists():
            nome = User.objects.get(email=email).username
            user = authenticate(request, username=nome, password=senha1)
            if user is not None:
                auth_login(request, user)
                return redirect('dashboard')
        messages.error(request, 'login inválido')
    return render(request, 'usuarios/login.html')


def dashboard(request):
    if request.user.is_authenticated:
        receitas = Receita.objects.order_by('-data_receita').filter(pessoa=request.user.id)

        dados = {
            'receitas': receitas

        }
        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')


def criar_receita(request):
    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita']
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
        return render(request, 'usuarios/criar_receita.html')


def edita_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita_a_editar = {
        'receita': receita
    }
    return render(request, 'usuarios/edita_receita.html', receita_a_editar)


def logout(request):
    auth_logout(request)
    return redirect('index')


def deleta_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita.delete()
    return redirect('dashboard')

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

def campo_vazio(campo):
    return not campo.strip()


def verifica_senha(senha1, senha2):
    return senha1 != senha2