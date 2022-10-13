from core.models import Sepultamento
from django.shortcuts import render, redirect
from core.forms import Jazigo, Obito, Sepultamento
from core.forms import FormJazigo, FormObito, FormSepultamento
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib import messages

def home(request):
    return render(request, 'core/index.html')

class Registrar(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registrar.html'
    
    

@login_required
def cadastro_jazigo(request):
    if request.user.is_staff and request.user.is_active:
        form = FormJazigo(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, f"Cadastro de jazigo da família {form.cleaned_data['nomeFamilia']} realizado com sucesso!")
            return redirect('url_listagem_jazigos')
        contexto = {'form': form, 'acao': 'Salvar', 'titulo': 'Jazigo'}
        return render(request, 'core/cadastro.html', contexto)
    else:
        return render(request, 'nao-autorizado.html')

@login_required
def cadastro_obito(request):
    if request.user.is_staff and request.user.is_active:
        form = FormObito(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, f"Cadastro de óbito de {form.cleaned_data['nome']} realizado com sucesso!")
            return redirect('url_listagem_obitos')
        contexto = {'form': form, 'acao': 'Salvar', 'titulo': 'Óbito'}
        return render(request, 'core/cadastro.html', contexto)
    else:
        return render(request, 'nao-autorizado.html')

@login_required
def cadastro_sepultamento(request):
    if request.user.is_staff and request.user.is_active:
        form = FormSepultamento(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, f"Cadastro de sepultamento de {form.cleaned_data['nome']} realizado com sucesso!")
            return redirect('url_listagem_sepultamentos')
        contexto = {'form': form, 'acao': 'Salvar', 'titulo': 'Sepultamento'}
        return render(request, 'core/cadastro.html', contexto)
    else:
        return render(request, 'nao-autorizado.html')


@login_required
def listagem_jazigos(request):
    if request.POST:
        if request.POST['pesquisa']:
            dados = Jazigo.objects.filter(nomeFamilia=request.POST['pesquisa'])
        else:
            dados = Jazigo.objects.all()
    else:
        dados = Jazigo.objects.all()
    contexto = {'dados': dados}
    return render(request, 'core/listagem/listagem-jazigos.html', contexto)

@login_required
def listagem_obitos(request):
    if request.POST:
        if request.POST['pesquisa']:
            dados = Obito.objects.filter(nomeFamilia=request.POST['pesquisa'])
        else:
            dados = Obito.objects.all()
    else:
        dados = Obito.objects.all()
    contexto = {'dados': dados}
    return render(request, 'core/listagem/listagem-obitos.html', contexto)

@login_required
def listagem_sepultamentos(request):
    if request.POST:
        if request.POST['pesquisa']:
            dados = Sepultamento.objects.filter(nomeFamilia=request.POST['pesquisa'])
        else:
            dados = Sepultamento.objects.all()
    else:
        dados = Sepultamento.objects.all()
    contexto = {'dados': dados}
    return render(request, 'core/listagem/listagem-sepultamentos.html', contexto)


@login_required
def atualiza_jazigo(request, id):
    if request.user.is_staff and request.user.is_active:
        obj = Jazigo.objects.get(id=id)
        form = FormJazigo(request.POST or None, request.FILES or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('url_listagem_jazigos')
        contexto = {'form': form, 'acao': 'Atualizar', 'titulo': 'Jazigo'}
        return render(request, 'core/cadastro.html', contexto)
    else:
        return render(request, 'nao-autorizado.html')

@login_required
def atualiza_obito(request, id):
    if request.user.is_staff and request.user.is_active:
        obj = Obito.objects.get(id=id)
        form = FormObito(request.POST or None, request.FILES or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('url_listagem_obitos')
        contexto = {'form': form, 'acao': 'Atualizar', 'titulo': 'Óbito'}
        return render(request, 'core/cadastro.html', contexto)
    else:
        return render(request, 'nao-autorizado.html')

@login_required
def atualiza_sepultamento(request, id):
    if request.user.is_staff and request.user.is_active:
        obj = Sepultamento.objects.get(id=id)
        form = FormSepultamento(request.POST or None, request.FILES or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('url_listagem_sepultamentos')
        contexto = {'form': form, 'acao': 'Atualizar', 'titulo': 'Sepultamento'}
        return render(request, 'core/cadastro.html', contexto)
    else:
        return render(request, 'nao-autorizado.html')


@login_required
def exclui_jazigo(request, id):
    if request.user.is_staff and request.user.is_active:
        obj = Jazigo.objects.get(id=id)
        contexto = {'dado': obj.nomeFamilia, 'classe': 'jazigo da família'}
        if request.POST:
            obj.delete()
            return redirect('url_listagem_jazigos')
        return render(request, 'core/confirma-exclusao.html', contexto)
    else:
        return render(request, 'nao-autorizado.html')

@login_required
def exclui_obito(request, id):
    if request.user.is_staff and request.user.is_active:
        obj = Obito.objects.get(id=id)
        contexto = {'dado': obj.nome, 'classe': 'óbito de'}
        if request.POST:
            obj.delete()
            return redirect('url_listagem_obitos')
        return render(request, 'core/confirma-exclusao.html', contexto)
    else:
        return render(request, 'nao-autorizado.html')

@login_required
def exclui_sepultamento(request, id):
    if request.user.is_staff and request.user.is_active:
        obj = Sepultamento.objects.get(id=id)
        contexto = {'dado': obj.nome, 'classe': 'sepultamento de'}
        if request.POST:
            obj.delete()
            return redirect('url_listagem_sepultamentos')
        return render(request, 'core/confirma-exclusao.html', contexto)
    else:
        return render(request, 'nao-autorizado.html')
