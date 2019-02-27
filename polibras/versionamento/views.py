from django.shortcuts import render

from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response

import logging

from .models import Empresa, Versao, Publicacao
from .serializers import EmpresaSerializer, VersaoSerializer, PublicacaoSerializer

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


def index(request):
    return render(request, 'versionamento/index.html')

def gerenciaEmpresa(request):
    return render(request, 'versionamento/empresa.html')

def gerenciaVersao(request):
    return render(request, 'versionamento/versao.html')

def gerenciaPublicacao(request):
    return render(request, 'versionamento/publicacao.html')

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
def criaEmpresa(request, format=None):
    if request.method == 'POST':
        nome = request.POST.get('nome_text', 'Empresa Teste')
        dados = {'nome': nome}
        
        serializer = EmpresaSerializer(data=dados)
        if serializer.is_valid():
            serializer.save()
            if status.HTTP_201_CREATED:
                logger.info('A empresa %s foi criada.', nome)
                return render(request, 'versionamento/sucesso.html')
        
        logger.error('Ocorreu um erro na criação da empresa %s.', nome)
        return render(request, 'versionamento/erro.html')

@api_view(['PUT', 'POST'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
def editaEmpresa(request, format=None):
    context = {'recurso': 'Empresa'}

    if request.method == 'PUT' or request.method == 'POST':
        try:
            chave = request.POST.get('id_text', 1)
            empresa = Empresa.objects.get(pk=chave)
        except Empresa.DoesNotExist:
            return render(request, 'versionamento/indisponivel.html', context) 

        identificador = request.POST.get('id_text', 1)
        nome = request.POST.get('nome_text', 'Empresa Teste')
        dados = {'id': identificador, 'nome': nome}
        
        serializer = EmpresaSerializer(empresa, data=dados)
        if serializer.is_valid():
            serializer.save()
            if status.HTTP_200_OK:
                logger.info('A empresa %s foi editada.', nome)
                return render(request, 'versionamento/sucesso.html', context)
        
        logger.error('Ocorreu um erro na edição da empresa %s.', nome)
        return render(request, 'versionamento/erro.html', context)

@api_view(['DELETE', 'POST'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
def excluiEmpresa(request, format=None):
    context = {'recurso': 'Empresa'}

    if request.method == 'DELETE' or request.method == 'POST':
        try:
            chave = request.POST.get('id_text', 1) 
            empresa = Empresa.objects.get(pk=chave)
        except Empresa.DoesNotExist:
            return render(request, 'versionamento/indisponivel.html', context)
        
        empresa.delete()
        if status.HTTP_204_NO_CONTENT:
            logger.info('A empresa %s foi excluída.', empresa.nome)
            return render(request, 'versionamento/sucesso.html', context)

        logger.error('Ocorreu um erro na exclusão da empresa %s.', empresa.nome)
        return render(request, 'versionamento/erro.html', context)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
def criaVersao(request, format=None):
    if request.method == 'POST':
        codigo = request.POST.get('arquivo_text', 'versaoteste.app')
        numero = request.POST.get('numero_text', 0)
        dados = {'codigo': codigo, 'numero': numero}
        
        serializer = VersaoSerializer(data=dados)
        if serializer.is_valid():
            serializer.save()
            if status.HTTP_201_CREATED:
                logger.info('A versão %s foi criada.', codigo)
                return render(request, 'versionamento/sucesso.html')

        logger.error('Ocorreu um erro na criação da versão %s.', codigo)
        return render(request, 'versionamento/erro.html')

@api_view(['PUT', 'POST'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
def editaVersao(request, format=None):
    context = {'recurso': 'Versão'}

    if request.method == 'PUT' or request.method == 'POST':
        try:
           chave = request.POST.get('id_text', 1)
           versao = Versao.objects.get(pk=chave)
        except Versao.DoesNotExist:
            return render(request, 'versionamento/indisponivel.html', context) 

        identificador = request.POST.get('id_text', 1)
        codigo = request.POST.get('arquivo_text', 'versaoteste.app')
        numero = request.POST.get('numero_text', 0)
        dados = {'id': identificador, 'codigo': codigo, 'numero': numero}
        
        serializer = VersaoSerializer(versao, data=dados)
        if serializer.is_valid():
            serializer.save()
            if status.HTTP_200_OK:
                logger.info('A versão %s foi editada.', codigo)
                return render(request, 'versionamento/sucesso.html', context)

        logger.error('Ocorreu um erro na edição da versão %s.', codigo)
        return render(request, 'versionamento/erro.html', context)

@api_view(['DELETE', 'POST'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
def excluiVersao(request, format=None):
    context = {'recurso': 'Versão'}

    if request.method == 'DELETE' or request.method == 'POST':
        try:
            chave = request.POST.get('id_text', 1)
            versao = Versao.objects.get(pk=chave)
        except Versao.DoesNotExist:
            return render(request, 'versionamento/indisponivel.html', context)
        
        versao.delete()
        if status.HTTP_204_NO_CONTENT:
            logger.info('A versão %s foi excluída.', versao.codigo)
            return render(request, 'versionamento/sucesso.html', context)

        logger.error('Ocorreu um erro na exclusão da versão %s.', versao.codigo)
        return render(request, 'versionamento/erro.html', context)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
def criaPublicacao(request, format=None):
    if request.method == 'POST':
        chave_versao = request.POST.get('versao_text', 1)
        try:
            versao = Versao.objects.get(pk=chave_versao)
        except Versao.DoesNotExist:
            context = {'recurso': 'Versão'}
            logger.info('A versão informada não existe.')
            return render(request, 'versionamento/indisponivel.html', context)

        if len(Publicacao.objects.all()) > 0:
           chave_empresa = request.POST.get('empresa_text', 1) 

           if len(Publicacao.objects.filter(empresa=chave_empresa)) > 0:           
              publicacao_mais_recente = Publicacao.objects.filter(empresa=chave_empresa).order_by('-data_pub')[0]
        
              versao_mais_recente_id = int(publicacao_mais_recente.versao.id)
              versao_atualizada_id = int(chave_versao)

              if versao_mais_recente_id < versao_atualizada_id:
                 data =  request.POST.get('data_text', '2011-11-11')
                 dados = {'data_pub': data, 'empresa': chave_empresa, 'versao': chave_versao}
           
                 serializer = PublicacaoSerializer(data=dados)
                 if serializer.is_valid():
                    serializer.save()
                    if status.HTTP_201_CREATED:
                       logger.info('A publicação foi criada.')
                       return render(request, 'versionamento/sucesso.html')
                 
                 logger.error('Ocorreu um erro na criação da publicação.')
                 return render(request, 'versionamento/erro.html')
              else:
                 logger.info('A empresa já possui a versão atualizada.')
                 context = {'mensagem': 'Versão já está atualizada.'}
                 return render(request, 'versionamento/mensagem.html', context)

        data =  request.POST.get('data_text', '2011-11-11')
        empresa = request.POST.get('empresa_text', 1) 
        dados = {'data_pub': data, 'empresa': empresa, 'versao': chave_versao}
           
        serializer = PublicacaoSerializer(data=dados)
        if serializer.is_valid():
           serializer.save()
           if status.HTTP_201_CREATED:
              logger.info('A publicação foi criada.')
              return render(request, 'versionamento/sucesso.html')

        logger.error('Ocorreu um erro na criação da publicação.')
        return render(request, 'versionamento/erro.html')

@api_view(['PUT', 'POST'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
def editaPublicacao(request, format=None):
    context = {'recurso': 'Publicação'}

    if request.method == 'PUT' or request.method == 'POST':
        try:
            chave = request.POST.get('id_text', 1)
            publicacao = Publicacao.objects.get(pk=chave)
        except Publicacao.DoesNotExist:
            logger.info('A publicação solicitada não existe.')
            return render(request, 'versionamento/indisponivel.html', context) 

        identificador = request.POST.get('id_text', 1)
        data = request.POST.get('data_text', '2011-11-11')
        empresa = request.POST.get('empresa_text', 1)
        versao = request.POST.get('versao_text', 1)
        dados = {'id': identificador, 'data_pub': data, 'empresa': empresa, 'versao': versao}
        
        serializer = PublicacaoSerializer(publicacao, data=dados)
        if serializer.is_valid():
            serializer.save()
            if status.HTTP_200_OK:
                logger.info('A publicação %s foi editada.', identificador)
                return render(request, 'versionamento/sucesso.html', context)
        
        logger.error('Ocorreu um erro na edição da publicação.')
        return render(request, 'versionamento/erro.html', context)

@api_view(['DELETE', 'POST'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
def excluiPublicacao(request, format=None):
    context = {'recurso': 'Publicação'}

    if request.method == 'DELETE' or request.method == 'POST':
        try:
            chave = request.POST.get('id_text', 1)
            publicacao = Publicacao.objects.get(pk=chave)
        except Publicacao.DoesNotExist:
            logger.info('A publicação solicitada não existe.')
            return render(request, 'versionamento/indisponivel.html', context)
        
        publicacao.delete()
        if status.HTTP_204_NO_CONTENT:
            logger.info('A publicação %s foi excluída.', chave)
            return render(request, 'versionamento/sucesso.html', context)

        logger.error('Ocorreu um erro na exclusão da publicação.')
        return render(request, 'versionamento/erro.html', context)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
def listaPublicacoes(request, format=None):
    if request.method == 'GET':
        publicacoes = Publicacao.objects.all().order_by('data_pub')
        context = {'publicacoes': publicacoes}
        
        logger.info('Solicitação de listagem de publicações.') 
        return render(request, 'versionamento/lista_publicacoes.html', context)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
def filtraPublicacoesPorData(request, format=None):
    if request.method == 'GET': 
        data = request.GET.get('data_text', '2011-11-11')
        
        publicacoes = Publicacao.objects.filter(data_pub=data)
        context = {'publicacoes': publicacoes}
  
        logger.info('Solicitação de listagem de publicações filtradas pela data %s.', data)
        return render(request, 'versionamento/lista_publicacoes.html', context)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
def filtraPublicacoesPorVersao(request, format=None):     
   if request.method == 'GET':
      versao = request.GET.get('versao_text', 1)
      try:
         Versao.objects.get(pk=versao)
      except Versao.DoesNotExist:
         logger.info('Versão solicitada não existe.')
         context = {'recurso': 'Versão'}
         return render(request, 'versionamento/indisponivel.html', context)
      
      publicacoes = Publicacao.objects.filter(versao=versao)
      context = {'publicacoes': publicacoes}

      logger.info('Solicitação de listagem de publicações filtradas pela versão %s.', versao)
      return render(request, 'versionamento/lista_publicacoes.html', context)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
def filtraPublicacoesPorEmpresa(request, format=None):     
   if request.method == 'GET':
      empresa = request.GET.get('empresa_text', 1)
      try:
         Empresa.objects.get(pk=empresa)
      except Empresa.DoesNotExist:
         logger.info('Empresa solicitada não existe.')
         context = {'recurso': 'Empresa'}
         return render(request, 'versionamento/indisponivel.html', context)
      
      publicacoes = Publicacao.objects.filter(empresa=empresa)
      context = {'publicacoes': publicacoes}
      
      logger.info('Solicitação de listagem de publicações filtradas pela empresa %s.', empresa)
      return render(request, 'versionamento/lista_publicacoes.html', context)
