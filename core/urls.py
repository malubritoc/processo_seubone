from django.contrib import admin
from django.urls import path, include
from .views import home, salvar, editar, atualizar, excluir, adicionar, tecidos_filtrados_referencia, tecidos_filtrados_tipo, tecidos_filtrados_cor, abrir_estoque, tecidos_filtrados_referencia_estoque, tecidos_filtrados_tipo_estoque, tecidos_filtrados_cor_estoque, voltar_inputs, ver_estoque, limpar_filtros_estoque, limpar_filtros

urlpatterns = [
    path('', home),
    path('adicionar', adicionar, name='adicionar'),
    path('salvar', salvar, name='salvar'),
    path('editar/<int:id>', editar, name='editar'),
    path('atualizar/<int:id>', atualizar, name='atualizar'),
    path('excluir/<int:id>', excluir, name='excluir'),
    path('tecidos_filtrados_referencia', tecidos_filtrados_referencia, name='tecidos_filtrados_referencia'),
    path('tecidos_filtrados_tipo', tecidos_filtrados_tipo, name='tecidos_filtrados_tipo'),
    path('tecidos_filtrados_cor', tecidos_filtrados_cor, name='tecidos_filtrados_cor'),
    path('abrir_estoque', abrir_estoque, name='abrir_estoque'),
    path('tecidos_filtrados_referencia_estoque', tecidos_filtrados_referencia_estoque, name='tecidos_filtrados_referencia_estoque'),
    path('tecidos_filtrados_tipo_estoque', tecidos_filtrados_tipo_estoque, name='tecidos_filtrados_tipo_estoque'),
    path('tecidos_filtrados_cor_estoque', tecidos_filtrados_cor_estoque, name='tecidos_filtrados_cor_estoque'),
    path('voltar_inputs', voltar_inputs, name='voltar_inputs'),
    path('ver_estoque', ver_estoque, name='ver_estoque'),
    path('limpar_filtros_estoque', limpar_filtros_estoque, name='limpar_filtros_estoque'),
    path('limpar_filtros', limpar_filtros, name='limpar_filtros'),
]