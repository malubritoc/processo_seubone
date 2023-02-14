from django.shortcuts import render, redirect
from .models import Tecido

def home(request):
    tecidos = Tecido.objects.all()
    return render(request, 'index.html', {'tecidos': tecidos})

def retornar_cores():
    return ['amarelo', 'vermelho', 'chumbo']

def retornar_tecidos():
    return ['Linho', 'Camurça', 'Mescla', 'Moletom']

def definir_referencia(tipo, cor):
    tipos_tecidos = retornar_tecidos()
    cores = retornar_cores()
    referencia = str(tipos_tecidos.index(tipo)+1).zfill(3)+str(cores.index(cor)+1).zfill(3)
    return referencia

def salvar(request):
    vtipo = request.POST.get('tipo')
    vcor = request.POST.get('cor')
    vreferencia = definir_referencia(vtipo, vcor)
    vmetragem = request.POST.get('metragem')
    Tecido.objects.create(referencia = vreferencia, tipo=vtipo, cor=vcor, metragem=vmetragem)
    return redirect(home)


def adicionar(request):
    #Adicionar cores na lista
    cores = retornar_cores()
    return render(request, 'add.html', {'cores': cores}) 
    

def editar (request, id): 
    cores = retornar_cores()
    tecido = Tecido.objects.get(id=id)
    return render (request, 'update.html', {'tecido': tecido, 'cores': cores})

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

