from datetime import timedelta
from django.shortcuts import render, redirect
from appHome.forms import FormAddLogin, FormLogin, FormProduto
from appHome.models import Login, Produto
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password


def appHome(request):

    email = request.session.get('email')

    if email:
        try:
            if Login.objects.get(email=email):
                prodList = Produto.objects.all().values()

                context = {
                    'produtos': prodList,
                }
                return render(request, "home.html", context)
        except Login.DoesNotExist:
            pass
    return redirect('fazerLogin')
    

def excluir_Produto(request, id_produto):
    produto = Produto.objects.get(id = id_produto)
    produto.delete()

    return redirect('appHome')


def add_Produto(request):
    
    if request.method == 'POST':
        formProduto = FormProduto(request.POST, request.FILES)
        if formProduto.is_valid():
            formProduto.save()
            return redirect('appHome')
    else:
        formProduto = FormProduto()

    context = {
        'form' : formProduto
    }
    return render(request, 'add_Produto.html', context)


def editar_Produto(request, id_produto):
    produto = Produto.objects.get(id=id_produto)
    if request.method == 'POST':
        form = FormProduto(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('appHome')
    else:
        form = FormProduto(instance=produto)
        
    context = {
        'form' : form
    }
    return render(request, 'editar_Produto.html', context)



def fazerLogin(request):
    formL = FormLogin(request.POST or None)
    if request.method == 'POST':
        if formL.is_valid():
            _email = formL.cleaned_data.get('email')
            _senha = formL.cleaned_data.get('senha')
            try:
                usuarioL = Login.objects.get(email=_email)
                if check_password(_senha, usuarioL.senha):
                    request.session.set_expiry(timedelta(seconds=600))
                    request.session['email'] = _email
                    messages.success(request, 'Login realizado com sucesso, bem-vindo(a) de volta {}!'.format(usuarioL.usuario))
                    return redirect('appHome')
                else:
                    messages.error(request, 'Credenciais inválidas. Por favor, tente novamente.')
            except Login.DoesNotExist:
                messages.error(request, 'Credenciais inválidas. Por favor, tente novamente.')
    context = {
        'formLogin': formL
    }
    return render(request, 'login.html', context)


def add_login(request):
    formAddL = FormAddLogin(request.POST or None)
    if request.method == 'POST':    
        if formAddL.is_valid():
            email = formAddL.cleaned_data.get('email')
            senha = formAddL.cleaned_data.get('senha')
            if Login.objects.filter(email=email).exists():
                messages.error(request, 'Este email já está sendo usado. Por favor, escolha outro.')
            else:
                
                formAddL.cleaned_data['senha'] = make_password(senha)
                Login.objects.create(
                    email=email,
                    senha=formAddL.cleaned_data['senha'],
                    usuario=formAddL.cleaned_data.get('usuario')
                )

                messages.success(request, 'Usuário adicionado com sucesso!')
                return redirect('fazerLogin')
    context = {
        'formAddLogin': formAddL
    }
    return render(request, 'add_login.html', context)


def mostrarProdutos (request):
    ultimos_produtos = Produto.objects.order_by('-id')[:8]  # Seleciona os últimos 8 produtos
    context = {'ultimos_produtos': ultimos_produtos}
    return render(request, 'pag_vendas.html', context)