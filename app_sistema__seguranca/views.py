# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
# from .forms import LoginForm
# from .models import Aluno, Funcionario
# import os
# from shutil import move


# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('index')  # Redirecione para a página 'index' após o login bem-sucedido
#     else:
#         form = LoginForm()
#     return render(request, 'front-end/login.html', {'form': form})

# def index(request):
#     return render(request, 'front-end/index.html')

# def cadastros(request):
#     return render(request, 'front-end/cadastros.html')

# from django.shortcuts import render, redirect
# from .models import Aluno, Funcionario

# def get_unique_filename(folder, filename):
#     path = os.path.join(folder, filename)
#     root, ext = os.path.splitext(path)
#     index = 1

#     while os.path.exists(path):
#         path = f"{root}_{index}{ext}"
#         index += 1

#     return path

# def cadastros(request):
#     if request.method == 'POST':
#         nome = request.POST['nome']
#         email = request.POST['email']
#         endereco = request.POST['endereco']
#         telefone = request.POST['telefone']
#         foto = request.FILES.get('foto')
#         bloqueado_type = request.POST.get('bloqueado_type')  # '1' para aluno, '2' para funcionário

#         if foto:
#             filename = foto.name
#             if bloqueado_type == '1':
#                 folder = 'Fotos/Aluno'
#             elif bloqueado_type == '2':
#                 folder = 'Fotos/Funcionario'
#             else:
#                 return redirect('index')

#             # Verifica se o arquivo com o mesmo nome já existe na pasta
#             if os.path.exists(os.path.join(folder, filename)):
#                 filename = get_unique_filename(folder, filename)

#             file_path = os.path.join(folder, filename)

#             # Salva o arquivo na pasta com o nome único
#             with open(file_path, 'wb') as destination:
#                 for chunk in foto.chunks()

#             # Salvar os dados do aluno ou funcionário no banco de dados
#             if bloqueado_type == '1':
#                 aluno = Aluno(nome=nome, email=email, endereco=endereco, telefone=telefone, foto=filename)
#                 aluno.save()
#             elif bloqueado_type == '2':
#                 funcionario = Funcionario(nome=nome, email=email, endereco=endereco, telefone=telefone, foto=filename)
#                 funcionario.save()

#         return redirect('index')


#     return render(request, 'front-end/cadastros.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .models import Aluno, Funcionario, Bloqueado, FotoBloqueado

from shutil import move


from django.views import View
#import cv2
#import face_recognition
import os
import numpy as np
#import pickle
from screeninfo import get_monitors
import serial
#from serial.tools import list_ports
#import time


from django.http import HttpResponse
#from app_sistema__seguranca.back_end.Reconhecimento_facial_WebCam import process_frame, display_fps, toggle_fullscreen

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index') 
    else:
        form = LoginForm()
    return render(request, 'front-end/login.html', {'form': form})

def index(request):
    return render(request, 'front-end/index.html')



def cadastros(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        endereco = request.POST['endereco']
        telefone = request.POST['telefone']
        pessoa_type = request.POST.get('pessoa_type')  # '1' para aluno, '2' para funcionário

        # Verificar se o campo 'foto' é um único arquivo ou vários arquivos
        fotos = request.FILES.getlist('foto')
        
        if pessoa_type == '1':
            folder = 'app_sistema__seguranca/back_end/dataset/Aluno'
        elif pessoa_type == '2':
            folder = 'app_sistema__seguranca/back_end/dataset/Funcionario'
        else:
            return redirect('index')

        # Criar o objeto Aluno ou Funcionário fora do loop das fotos
        if pessoa_type == '1':
            aluno = Aluno(nome=nome, email=email, endereco=endereco, telefone=telefone)
        elif pessoa_type == '2':
            funcionario = Funcionario(nome=nome, email=email, endereco=endereco, telefone=telefone)

        # Percorrer as fotos e associar cada uma ao objeto Aluno ou Funcionário
        for foto in fotos:
            i = 1  # Inicialize 'i' para evitar o erro
            filename = f"{nome}_{i}"
            
            while os.path.exists(os.path.join(folder, f"{filename}.jpg")):
                i += 1
                filename = f"{nome}_{i}"
                
            filename = f"{filename}.jpg"
            file_path = os.path.join(folder, filename)

            # Salvar o arquivo na pasta com o nome único
            with open(file_path, 'wb') as destination:
                for chunk in foto.chunks():
                    destination.write(chunk)

            # Associar a foto ao objeto Aluno ou Funcionário
            if pessoa_type == '1':
                aluno.foto = filename
            elif pessoa_type == '2':
                funcionario.foto = filename

        # Salvar o objeto Aluno ou Funcionário após associar todas as fotos
        if pessoa_type == '1':
            aluno.save()
        elif pessoa_type == '2':
            funcionario.save()

        return redirect('cadastros')

    return render(request, 'front-end/cadastros.html')





#Cadastro bloqueados Bloqueadas


import os
from django.conf import settings

def bloquear(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        endereco = request.POST.get('endereco')
        telefone = request.POST.get('telefone')
        descricao = request.POST.get('descricao')

        bloqueado = Bloqueado.objects.create(nome=nome, email=email, endereco=endereco, telefone=telefone, descricao=descricao)

        fotos = request.FILES.getlist('foto')
        for index, foto in enumerate(fotos):
            # Renomear a foto
            nome_foto = f'{nome}_{index + 1}.jpg'
            
            # Salvar a foto no diretório dataset/Bloqueado
            path_foto = os.path.join(settings.BASE_DIR, 'app_sistema__seguranca', 'back_end', 'dataset', 'Bloqueado', nome_foto)
            with open(path_foto, 'wb+') as destination:
                for chunk in foto.chunks():
                    destination.write(chunk)

        return redirect('bloquear') 
    return render(request, 'front-end/bloquear.html')



#inicio reconhecimento facial WebCam - Modo Bloqueio
from app_sistema__seguranca.back_end.Reconhecimento_facial_WebCam_BLOQUEIO_MODE import webcamBloq

def protecao(request):
      
    webcamBloq(request)  
  
    return redirect('index')
#Fim reconhecimento facial WebCam - Modo BloqueiowebcamBloq



#inicio reconhecimento facial camera ip- Modo Bloqueio
from app_sistema__seguranca.back_end.Reconhecimento_facial_Cam_IP_Bloqueio import camIP_Bloq

def protecao2(request):
      
    ip = "192.168.1.150"
    port = 554

    if testar_conexao(ip, port):
        try:
            camIP_Bloq(request)
        except Exception as e:
            return redirect('alerta')
    else:
        return redirect('alerta')
    
    return redirect('index')
#Fim reconhecimento facial camip - Modo Bloqueio


#inicio reconhecimento facial WebCam - Modo Bloqueio
from app_sistema__seguranca.back_end.Reconhecimento_facial_WebCam import webcam 
def reconhecimento(request):

    webcam(request)
 
    return redirect('index')


#Fim reconhecimento facial WebCam - Modo Controle de acesso
def alerta_view(request):
    return render(request, 'front-end/alerta.html')

#inicio reconhecimento facial camip - Modo Bloqueio
from app_sistema__seguranca.back_end.Reconhecimento_facial_Cam_IP import camIP
# def reconhecimento2(request):


    # camera_offline = True  # Defina como True se a câmera estiver offline

    # # Processamento da imagem
    # if camera_offline:
    #     # Se a câmera estiver offline, envie uma mensagem para o template
    #     message = "Câmera offline. Por favor, verifique a conexão."
    #     return render(request, 'front-end/alerta.html', {'message': message})
    # else:



    # camIP(request)
 
    # return redirect('index')
    
    
        # try:
        #     camIP(request)
        # except Exception as e:
        #     error_message = str(e)
        #     if "failed: Network is unreachable" in error_message:
        #         return redirect('alerta')
        
        # return redirect('index')


import socket
from django.shortcuts import redirect

def testar_conexao(host, port):
    try:
        socket.setdefaulttimeout(1)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.close()
        return True
    except (socket.timeout, socket.error):
        return False

def reconhecimento2(request):
    ip = "192.168.1.150"
    port = 554

    if testar_conexao(ip, port):
        try:
            camIP(request)
        except Exception as e:
            return redirect('alerta')
    else:
        return redirect('alerta')
    
    return redirect('index')






#Fim reconhecimento facial camip - Modo Controle de acesso


def sincronizar(request):
    
    return render(request, 'front-end/sincronizar.html')


# from django.http import JsonResponse
from django.shortcuts import render
from app_sistema__seguranca.back_end.detector_faces import sincron
def sincronizacao(request):
    
    
    sincron(request)
 
    return redirect('index')





from app_sistema__seguranca.models import Aluno, Funcionario, Bloqueado
   
def index(request):
    total_alunos = Aluno.objects.count()
    total_funcionarios = Funcionario.objects.count()
    total_bloqueados = Bloqueado.objects.count()

    return render(request, 'front-end/index.html', {
        'total_alunos': total_alunos,
        'total_funcionarios': total_funcionarios,
        'total_bloqueados': total_bloqueados,
    })