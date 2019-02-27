from django.contrib import admin

from .models import Empresa, Versao, Publicacao

admin.site.register(Empresa)
admin.site.register(Versao)
admin.site.register(Publicacao)
