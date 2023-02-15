from django.shortcuts import render, redirect
from .models import Tecido
from .forms import FiltroTecidosReferenciaForm, FiltroTecidosTipoForm, FiltroTecidosCorForm
from django.db.models import Sum
from math import floor

def home(request):
    tecidos = Tecido.objects.all()
    return render(request, 'index.html', {'tecidos': tecidos})

def retornar_tecidos():
    return ['Linho', 'Camurça', 'Mescla', 'Moletom']
    
def retornar_cores():
    return ['Branco', 'Preto', 'Cinza', 'Chumbo', 'Vermelho', 'Vinho', 'Coral', 'Laranja', 'Amarelo', 'Amarelo Canário', 'Amarelo Neon', 'Marrom', 'Caramelo', 'Caqui', 'Bege', 'Rosa Bebê', 'Rosa Neon', 'Pink', 'Azul Claro', 'Azul Turquesa', 'Azul Royal', 'Azul Marinho', 'Roxo', 'Verde Lodo', 'Verde Sinuca', 'Verde Bandeira', 'Verde Limão', 'Verde Água']


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
    tipos_tecidos = retornar_tecidos()
    return render(request, 'add.html', {'cores': cores, 'tipos_tecidos': tipos_tecidos}) 
    

def editar (request, id): 
    cores = retornar_cores()
    tecido = Tecido.objects.get(id=id)
    return render (request, 'update.html', {'tecido': tecido, 'cores': cores})

def atualizar(request, id):
    vtipo = request.POST.get('tipo')
    vcor = request.POST.get('cor')
    vmetragem = request.POST.get('metragem')
    vreferencia = definir_referencia(vtipo,vcor)
    tecido = Tecido.objects.get(id=id)
    tecido.tipo = vtipo
    tecido.cor = vcor
    tecido.metragem = vmetragem
    tecido.referencia = vreferencia
    tecido.save()
    return redirect(home)

def excluir (request, id): 
    tecido = Tecido.objects.get(id=id)
    tecido.delete()
    return redirect(home)

def tecidos_filtrados_referencia(request):
    form = FiltroTecidosReferenciaForm(request.GET)
    tecidos = Tecido.objects.all()
    if form.is_valid():
        if form.cleaned_data['referencia']:
            tecidos = tecidos.filter(referencia__icontains=form.cleaned_data['referencia'])
        return render(request, 'index.html', {'form': form, 'tecidos': tecidos})     
        
def tecidos_filtrados_tipo(request): 
    print(request) 
    form = FiltroTecidosTipoForm(request.GET)
    tecidos = Tecido.objects.all()
    if form.is_valid():      
        if form.cleaned_data['tipo']:
            tecidos = tecidos.filter(tipo__icontains=form.cleaned_data['tipo'])
        return render(request, 'index.html', {'form': form, 'tecidos': tecidos})
        
def tecidos_filtrados_cor(request):
    form = FiltroTecidosCorForm(request.GET)
    tecidos = Tecido.objects.all()
    if form.is_valid():
        if form.cleaned_data['cor']:
            tecidos = tecidos.filter(cor__icontains=form.cleaned_data['cor'])
    return render(request, 'index.html', {'form': form, 'tecidos': tecidos})   

def limpar_filtros(request):
    return redirect(home)

def producao(tecidos_list):
    prod_total = 0
    for tecido in tecidos_list:
        tecido['producao'] = floor(float(tecido['metragem_total']) * 7)
        prod_total += tecido['producao']
    return tecidos_list, prod_total

def ver_estoque():
    tecidos = Tecido.objects.values('referencia', 'tipo', 'cor').annotate(metragem_total=Sum('metragem'))
    tecidos_list = list(tecidos)
    tecidos_list, prod_total = producao(tecidos_list)
    return tecidos_list, prod_total

def abrir_estoque(request):
    tecidos_list, prod_total = ver_estoque()
    return render (request, 'estoque.html', {'tecidos': tecidos_list, 'prod_total': prod_total})

def limpar_filtros_estoque(request):
    tecidos_list, prod_total = ver_estoque()
    return render (request, 'estoque.html', {'tecidos': tecidos_list, 'prod_total': prod_total})

def tecidos_filtrados_referencia_estoque(request):
    form = FiltroTecidosReferenciaForm(request.GET)
    tecidos_list, prod_total = ver_estoque()
    if form.is_valid():
        if form.cleaned_data['referencia']:
            tecidos = Tecido.objects.values('referencia', 'tipo', 'cor').annotate(metragem_total=Sum('metragem'))
            tecidos = tecidos.filter(referencia__icontains=form.cleaned_data['referencia'])
            tecidos_list = list(tecidos)
            tecidos_list, prod_total = producao(tecidos_list)
    return render(request, 'estoque.html', {'form': form, 'tecidos': tecidos_list, 'prod_total': prod_total})  
        
def tecidos_filtrados_tipo_estoque(request):  
    form = FiltroTecidosTipoForm(request.GET)
    tecidos_list, prod_total = ver_estoque()
    if form.is_valid():
        if form.cleaned_data['tipo']:
            tecidos = Tecido.objects.values('referencia', 'tipo', 'cor').annotate(metragem_total=Sum('metragem'))
            tecidos = tecidos.filter(tipo__icontains=form.cleaned_data['tipo'])
            tecidos_list = list(tecidos)
            tecidos_list, prod_total = producao(tecidos_list)
    return render(request, 'estoque.html', {'form': form, 'tecidos': tecidos_list, 'prod_total': prod_total}) 
        
def tecidos_filtrados_cor_estoque(request):
    form = FiltroTecidosCorForm(request.GET)
    tecidos_list, prod_total = ver_estoque()
    if form.is_valid():
        if form.cleaned_data['cor']:
            tecidos = Tecido.objects.values('referencia', 'tipo', 'cor').annotate(metragem_total=Sum('metragem'))
            tecidos = tecidos.filter(cor__icontains=form.cleaned_data['cor'])
            tecidos_list = list(tecidos)
            tecidos_list, prod_total = producao(tecidos_list)
    return render(request, 'estoque.html', {'form': form, 'tecidos': tecidos_list, 'prod_total': prod_total}) 


def voltar_inputs(request):
    return redirect(home)

