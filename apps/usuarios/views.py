from django.shortcuts import render, redirect
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


def logout(request):
    auth_logout(request)
    return redirect('index')


def campo_vazio(campo):
    return not campo.strip()


def verifica_senha(senha1, senha2):
    return senha1 != senha2