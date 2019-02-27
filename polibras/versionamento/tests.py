from django.test import TestCase
from django.http import HttpRequest
from .views import criaEmpresa, editaEmpresa, excluiEmpresa, criaVersao, editaVersao, excluiVersao, criaPublicacao, editaPublicacao, excluiPublicacao, listaPublicacoes, filtraPublicacoesPorData, filtraPublicacoesPorVersao, filtraPublicacoesPorEmpresa 

class EmpresaTestes(TestCase):
   requisicao = HttpRequest()
   requisicao.method = 'POST'

   def testeCriaEmpresa(self):
      resposta = criaEmpresa(self.requisicao) 
      self.assertEqual(resposta.status_code, 200)

   def testeEditaEmpresa(self):
      criaEmpresa(self.requisicao)

      resposta = editaEmpresa(self.requisicao) 
      self.assertEqual(resposta.status_code, 200) 

   def testeExcluiEmpresa(self):
      criaEmpresa(self.requisicao)

      resposta = excluiEmpresa(self.requisicao) 
      self.assertEqual(resposta.status_code, 200)

class VersaoTestes(TestCase):
   requisicao = HttpRequest()
   requisicao.method = 'POST'

   def testeCriaVersao(self):
      resposta = criaVersao(self.requisicao)
      self.assertEqual(resposta.status_code, 200) 

   def testeEditaVersao(self):
      criaVersao(self.requisicao)
      
      resposta = editaVersao(self.requisicao)
      self.assertEqual(resposta.status_code, 200)

   def testeexcluiVersao(self):
      criaVersao(self.requisicao)

      resposta = excluiVersao(self.requisicao)
      self.assertEquals(resposta.status_code, 200)

class PublicacaoTestes(TestCase):
   requisicao_post = HttpRequest()
   requisicao_post.method = 'POST'

   requisicao_get = HttpRequest()
   requisicao_get.method = 'GET'

   def testeCriaPublicacao(self):
      criaEmpresa(self.requisicao_post)
      criaVersao(self.requisicao_post)

      resposta = criaPublicacao(self.requisicao_post)
      self.assertEqual(resposta.status_code, 200)

   def testeEditaPublicacao(self):
      criaEmpresa(self.requisicao_post)
      criaVersao(self.requisicao_post)

      resposta = editaPublicacao(self.requisicao_post)
      self.assertEqual(resposta.status_code, 200) 

   def testeExcluiPublicacao(self):
      criaEmpresa(self.requisicao_post)
      criaVersao(self.requisicao_post)

      resposta = excluiPublicacao(self.requisicao_post)
      self.assertEqual(resposta.status_code, 200)

   def testeListaPublicacoes(self):
      criaEmpresa(self.requisicao_post)
      criaVersao(self.requisicao_post)
      criaPublicacao(self.requisicao_post)

      resposta = listaPublicacoes(self.requisicao_get)
      self.assertEqual(resposta.status_code, 200)

   def testeFiltraPublicacoesPorData(self):
      criaEmpresa(self.requisicao_post)
      criaVersao(self.requisicao_post)
      criaPublicacao(self.requisicao_post)

      resposta = filtraPublicacoesPorData(self.requisicao_get)
      self.assertEqual(resposta.status_code, 200)
   
   def testeFiltraPublicacoesPorVersao(self):
      criaEmpresa(self.requisicao_post)
      criaVersao(self.requisicao_post)
      criaPublicacao(self.requisicao_post)

      resposta = filtraPublicacoesPorVersao(self.requisicao_get)
      self.assertEqual(resposta.status_code, 200)
      
   def testeFiltraPublicacoesPorEmpresa(self):
      criaEmpresa(self.requisicao_post)
      criaVersao(self.requisicao_post)
      criaPublicacao(self.requisicao_post)

      resposta = filtraPublicacoesPorEmpresa(self.requisicao_get)
      self.assertEqual(resposta.status_code, 200)
