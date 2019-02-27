from django.urls import path
from . import views

urlpatterns = [
     #URLs páginas iniciais
     path('', views.index, name='index'),
     path('empresas/', views.gerenciaEmpresa, name='empresa'),
     path('versoes/', views.gerenciaVersao, name='versao'),
     path('publicacoes/', views.gerenciaPublicacao, name='publicacao'),
     
     #URLs página Empresas
     path('empresas/criar/', views.criaEmpresa, name='cria_empresa'),
     path('empresas/editar/', views.editaEmpresa, name='edita_empresa'),
     path('empresas/excluir/', views.excluiEmpresa, name='exclui_empresa'),     

     #URLs página Versões
     path('versoes/criar/', views.criaVersao, name='cria_versao'),
     path('versoes/editar/', views.editaVersao, name='edita_versao'),
     path('versoes/excluir/', views.excluiVersao, name='exclui_versao'),

     #URLs página Publicações
     path('publicacoes/criar/', views.criaPublicacao, name='cria_publicacao'),
     path('publicacoes/editar/', views.editaPublicacao, name='edita_publicacao'),
     path('publicacoes/excluir/', views.excluiPublicacao, name='exclui_publicacao'),
     path('publicacoes/listar/', views.listaPublicacoes, name='lista_publicacoes'),
     path('publicacoes/filtrar_por_data/', views.filtraPublicacoesPorData, name='filtra_por_data'),
     path('publicacoes/filtrar_por_versao/', views.filtraPublicacoesPorVersao, name='filtra_por_versao'),
     path('publicacoes/filtrar_por_empresa/', views.filtraPublicacoesPorEmpresa, name='filtra_por_empresa')
]
