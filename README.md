# Gestor de Versões
Gestor de versões de código para empresas desenvolvido com linguagem Python e framework Django.

O servidor deve ser executado localmente, mas pode ser alterado para hospedagem em serviço de nuvem.

O banco de dados sqlite3 possui alguns registros salvos, mas pode ser substituído por outro.


### Pré-requisitos para executar o sistema:
* Python >= 3
* Django >= 2
* django rest_framework


### Para executar o Servidor localmente
#### Abra o prompt de comando e digite os comandos abaixo:
* cd <caminho-onde-pasta-foi-extraida>/gestor_versoes/polibras/
* python manage.py runserver


### Para executar a aplicação Cliente
#### Abra o navegador e digite o seguinte endereço:
localhost:8000/versionamento/


### Para executar os Testes de Unidade
#### Abra o prompt de comando e digite:
* cd <caminho-onde-pasta-foi-extraida>/gestor_versoes/polibras/
* python manage.py test versionamento
