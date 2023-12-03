#!/bin/bash

# Caminho para o diretório do seu projeto Django
PROJECT_DIR=~/Documentos/TCC/projeto_sistema_de_seguranca/

# Ative o ambiente virtual se estiver usando um
source ~/caminho/para/seu/ambiente_virtual/bin/activate

# Navegue até o diretório do seu projeto
cd $PROJECT_DIR

# Inicie o servidor Django no próprio terminal
gnome-terminal -- python3 manage.py runserver

# Espere um momento para o servidor iniciar completamente
sleep 5

# Abra o navegador com o link http://127.0.0.1:8000/
xdg-open http://127.0.0.1:8000/

