from django.shortcuts import render, redirect
from .models import Tecido

def home(request):
    tecidos = Tecido.objects.all()
    return render(request, 'index.html', {'tecidos': tecidos})

def salvar(request):
    vtipo = request.POST.get('tipo')
    vcor = request.POST.get('cor')
    vmetragem = request.POST.get('metragem')
    Tecido.objects.create(tipo=vtipo, cor=vcor, metragem=vmetragem)
    tecidos = Tecido.objects.all()
    return render(request, 'index.html', {'tecidos': tecidos})

def editar (request, id): 
    tecido = Tecido.objects.get(id=id)
    return render (request, 'update.html', {'tecido': tecido})

def atualizar(request, id):
    vtipo = request.POST.get('tipo')
    vcor = request.POST.get('cor')
    vmetragem = request.POST.get('metragem')
    tecido = Tecido.objects.get(id=id)
    tecido.tipo = vtipo
    tecido.cor = vcor
    tecido.metragem = vmetragem
    tecido.save()
    return redirect(home)

def excluir (request, id): 
    tecido = Tecido.objects.get(id=id)
    tecido.delete()
    return redirect(home)