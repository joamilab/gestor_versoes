from django.db import models

class Empresa(models.Model):
    nome = models.CharField(max_length=200)


class Versao(models.Model):
    codigo = models.CharField(max_length=300)
    numero = models.IntegerField(default=1)


class Publicacao(models.Model):
    data_pub = models.DateField()
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    versao = models.ForeignKey(Versao, on_delete=models.CASCADE)
