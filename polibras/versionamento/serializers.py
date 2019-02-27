from rest_framework import serializers
from .models import Empresa, Versao, Publicacao


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class VersaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Versao
        fields = ('codigo', 'numero')

class PublicacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacao
        fields = ('data_pub', 'empresa', 'versao')

