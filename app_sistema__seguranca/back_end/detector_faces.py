
# import pickle
# import face_recognition
# import os
# import cv2
# import dlib

# # Função para exibir a barra de progresso
# def print_progress_bar(iteration, total, bar_length=50):
#     progress = (iteration / total)
#     arrow = '=' * int(round(bar_length * progress))
#     spaces = ' ' * (bar_length - len(arrow))
#     percent = progress * 100
#     print(f'[{arrow + spaces}] {percent:.2f}%', end='\r')

# # Função para carregar as imagens de uma pasta e retornar as codificações faciais e nomes
# def load_images_from_folder(folder, model='large', num_jitters=50, progress_callback=None):
#     face_encodings = []
#     face_names = []
#     total_files = len(os.listdir(folder))

#     for i, filename in enumerate(os.listdir(folder)):
#         img_path = os.path.join(folder, filename)
#         image = face_recognition.load_image_file(img_path)
#         encoding = face_recognition.face_encodings(image, num_jitters=num_jitters, model=model)
#         if encoding:
#             face_encodings.append(encoding[0])
#             face_names.append(f'{folder}: {filename}')  # Ele atribui o nome da pasta ao nome da pessoa onde a foto está.

#         if progress_callback:
#             progress_callback(i + 1, total_files)

#     return face_encodings, face_names

# # Carregar as imagens de todas as pastas
# all_face_encodings = []
# all_face_names = []

# def update_progress_bar(iteration, total_files):
#     print_progress_bar(iteration, total_files)

# model = 'large'  # Use o modelo 'large' para maior precisão


# #Para que o algoritmo crie várias versões "trejeitadas" da imagem, onde ele aplica pequenas rotações, deslocamentos e variações na iluminação.
# num_jitters = 50  # Aplique quantas iterações forem necessário (pode ajustar conforme necessário). 

# print("Carregando imagens da pasta 'aluno':")
# aluno_face_encodings, aluno_face_names = load_images_from_folder("dataset/aluno", model=model, num_jitters=num_jitters, progress_callback=update_progress_bar)
# print("\nCarregando imagens da pasta 'Funcionario':")
# funcionario_face_encodings, funcionario_face_names = load_images_from_folder("dataset/Funcionario", model=model, num_jitters=num_jitters, progress_callback=update_progress_bar)
# print("\nCarregando imagens da pasta 'Bloqueado':")
# bloqueado_face_encodings, bloqueado_face_names = load_images_from_folder("dataset/Bloqueado", model=model, num_jitters=num_jitters, progress_callback=update_progress_bar)

# all_face_encodings = aluno_face_encodings + funcionario_face_encodings + bloqueado_face_encodings
# all_face_names = aluno_face_names + funcionario_face_names + bloqueado_face_names

# # Defina o caminho para o arquivo pickle
# output_folder = 'output'
# os.makedirs(output_folder, exist_ok=True)
# pickle_file_path = os.path.join(output_folder, 'face_decodificada.pickle')

# # Salvar as informações em um arquivo pickle
# data_to_save = {
#     'all_face_encodings': all_face_encodings,
#     'all_face_names': all_face_names,
# }

# with open(pickle_file_path, 'wb') as file:
#     pickle.dump(data_to_save, file)

# # Carregar as informações do arquivo
# def load_face_encodings(pickle_file_path):
#     try:
#         with open(pickle_file_path, 'rb') as file:
#             data_loaded = pickle.load(file)
#             return data_loaded
#     except FileNotFoundError:
#         # Se o arquivo não existir, retorne None
#         return None

# # Carregar as informações do arquivo
# loaded_data = load_face_encodings(pickle_file_path)

# # Exemplo de uso das informações carregadas
# if loaded_data:
#     print("\nTotal de Face Decodificadas:", len(loaded_data['all_face_encodings']))
#     print("\nTotal de Nomes Encontrados:", len(loaded_data['all_face_names']))
#     # Você pode usar as informações conforme necessário
# else:
#     print("Arquivo .pickle não encontrado.")



# import pickle
# import face_recognition
# import os
# import cv2
# import dlib

# # Carregue o modelo shape_predictor_81_face_landmarks.dat
# predictor = dlib.shape_predictor('modelo_deteccao/shape_predictor_81_face_landmarks.dat')


# # Função para exibir a barra de progresso
# def print_progress_bar(iteration, total, bar_length=50):
#     progress = (iteration / total)
#     arrow = '=' * int(round(bar_length * progress))
#     spaces = ' ' * (bar_length - len(arrow))
#     percent = progress * 100
#     print(f'[{arrow + spaces}] {percent:.2f}%', end='\r')

# # Função para carregar as imagens de uma pasta e retornar as codificações faciais e nomes
# def load_images_from_folder(folder, model='large', num_jitters=50, progress_callback=None):
#     face_encodings = []
#     face_names = []
#     total_files = len(os.listdir(folder))

#     for i, filename in enumerate(os.listdir(folder)):
#         img_path = os.path.join(folder, filename)
#         image = face_recognition.load_image_file(img_path)
#         encoding = face_recognition.face_encodings(image, num_jitters=num_jitters, model=model)
#         if encoding:
#             face_encodings.append(encoding[0])
#             file_name, file_extension = os.path.splitext(filename)  # Divide o nome do arquivo e a extensão
#             face_names.append(f'{folder}: {file_name}')  # Ele atribui o nome da pasta ao nome da pessoa onde a foto está.

#         if progress_callback:
#             progress_callback(i + 1, total_files)

#     return face_encodings, face_names

# # Carregar as imagens de todas as pastas
# all_face_encodings = []
# all_face_names = []

# def update_progress_bar(iteration, total_files):
#     print_progress_bar(iteration, total_files)

# model = 'large'  # Use o modelo 'large' para maior precisão


# #Para que o algoritmo crie várias versões "trejeitadas" da imagem, onde ele aplica pequenas rotações, deslocamentos e variações na iluminação.
# num_jitters = 50  # Aplique quantas iterações forem necessário (pode ajustar conforme necessário). 

# print("Carregando imagens da pasta 'aluno':")
# aluno_face_encodings, aluno_face_names = load_images_from_folder("dataset/aluno", model=model, num_jitters=num_jitters, progress_callback=update_progress_bar)
# print("\nCarregando imagens da pasta 'Funcionario':")
# funcionario_face_encodings, funcionario_face_names = load_images_from_folder("dataset/Funcionario", model=model, num_jitters=num_jitters, progress_callback=update_progress_bar)
# print("\nCarregando imagens da pasta 'Bloqueado':")
# bloqueado_face_encodings, bloqueado_face_names = load_images_from_folder("dataset/Bloqueado", model=model, num_jitters=num_jitters, progress_callback=update_progress_bar)

# all_face_encodings = aluno_face_encodings + funcionario_face_encodings + bloqueado_face_encodings
# all_face_names = aluno_face_names + funcionario_face_names + bloqueado_face_names

# # Defina o caminho para o arquivo pickle
# output_folder = 'output'
# os.makedirs(output_folder, exist_ok=True)
# pickle_file_path = os.path.join(output_folder, 'face_decodificada.pickle')

# # Salvar as informações em um arquivo pickle
# data_to_save = {
#     'all_face_encodings': all_face_encodings,
#     'all_face_names': all_face_names,
# }

# with open(pickle_file_path, 'wb') as file:
#     pickle.dump(data_to_save, file)

# # Carregar as informações do arquivo
# def load_face_encodings(pickle_file_path):
#     try:
#         with open(pickle_file_path, 'rb') as file:
#             data_loaded = pickle.load(file)
#             return data_loaded
#     except FileNotFoundError:
#         # Se o arquivo não existir, retorne None
#         return None

# # Carregar as informações do arquivo
# loaded_data = load_face_encodings(pickle_file_path)

# # Exemplo de uso das informações carregadas
# if loaded_data:
#     print("\nTotal de Face Decodificadas:", len(loaded_data['all_face_encodings']))
#     print("\nTotal de Nomes Encontrados:", len(loaded_data['all_face_names']))
#     # Você pode usar as informações conforme necessário
# else:
#     print("Arquivo .pickle não encontrado.")


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from shutil import move
from django.views import View



import numpy as np


from django.http import JsonResponse

from django.http import HttpResponse



import pickle
import face_recognition
import os
import dlib
import face_recognition_models



# Carregue o modelo shape_predictor_81_face_landmarks.dat
predictor = dlib.shape_predictor('app_sistema__seguranca/back_end/modelo_deteccao/shape_predictor_81_face_landmarks.dat')

# Inicialização do detector facial e preditores
face_detector = dlib.get_frontal_face_detector()

preditor_68_point_model = face_recognition_models.pose_predictor_model_location()
pose_predictor_68_point = dlib.shape_predictor(preditor_68_point_model)

preditor_5_point_model = face_recognition_models.pose_predictor_five_point_model_location()
pose_predictor_5_point = dlib.shape_predictor(preditor_5_point_model)

cnn_face_detection_model = face_recognition_models.cnn_face_detector_model_location()
cnn_face_detector = dlib.cnn_face_detection_model_v1(cnn_face_detection_model)

face_recognition_model = face_recognition_models.face_recognition_model_location()
face_encoder = dlib.face_recognition_model_v1(face_recognition_model)



def sincron(request):




    # Função para exibir a barra de progresso
    def print_progress_bar(iteration, total, bar_length=50):
        progress = (iteration / total)
        arrow = '=' * int(round(bar_length * progress))
        spaces = ' ' * (bar_length - len(arrow))
        percent = progress * 100
        print(f'[{arrow + spaces}] {percent:.2f}%', end='\r')

    # Função para carregar as imagens de uma pasta e retornar as codificações faciais e nomes
    def load_images_from_folder(folder, model='large', num_jitters=1, progress_callback=None):
        face_encodings = []
        face_names = []
        total_files = len(os.listdir(folder))
        unrecognized_photos = []  # Lista para armazenar fotos não reconhecidas
        scanned_photos = 0  # Contador para fotos escaneadas

        for i, filename in enumerate(os.listdir(folder)):
            img_path = os.path.join(folder, filename)
            image = face_recognition.load_image_file(img_path)
            encoding = face_recognition.face_encodings(image, num_jitters=num_jitters, model=model)
            if encoding:
                face_encodings.append(encoding[0])
                file_name, file_extension = os.path.splitext(filename)
                face_names.append(f'{folder}: {file_name}')
            else:
                unrecognized_photos.append(filename)

            if progress_callback:
                progress_callback(i + 1, total_files)

            scanned_photos += 1

        return face_encodings, face_names, unrecognized_photos, scanned_photos

    # Carregar as imagens de todas as pastas
    all_face_encodings = []
    all_face_names = []

    def update_progress_bar(iteration, total_files):
        print_progress_bar(iteration, total_files)

    model = 'large'  # Use o modelo 'large' para maior precisão


    #Para que o algoritmo crie várias versões "trejeitadas" da imagem, onde ele aplica pequenas rotações, deslocamentos e variações na iluminação.
    num_jitters = 1  # Aplique quantas iterações forem necessário (pode ajustar conforme necessário). 

    print("Carregando imagens da pasta 'Aluno':")
    aluno_face_encodings, aluno_face_names, unrecognized_aluno, scanned_aluno = load_images_from_folder("app_sistema__seguranca/back_end/dataset/Aluno", model=model, num_jitters=num_jitters, progress_callback=update_progress_bar)
    print("\nCarregando imagens da pasta 'Funcionario':")
    funcionario_face_encodings, funcionario_face_names, unrecognized_funcionario, scanned_funcionario = load_images_from_folder("app_sistema__seguranca/back_end/dataset/Funcionario", model=model, num_jitters=num_jitters, progress_callback=update_progress_bar)
    print("\nCarregando imagens da pasta 'Bloqueado':")
    bloqueado_face_encodings, bloqueado_face_names, unrecognized_bloqueado, scanned_bloqueado = load_images_from_folder("app_sistema__seguranca/back_end/dataset/Bloqueado", model=model, num_jitters=num_jitters, progress_callback=update_progress_bar)

    all_face_encodings = aluno_face_encodings + funcionario_face_encodings + bloqueado_face_encodings
    all_face_names = aluno_face_names + funcionario_face_names + bloqueado_face_names


    # Defina o caminho para o arquivo pickle
    output_folder = 'app_sistema__seguranca/back_end/output'
    os.makedirs(output_folder, exist_ok=True)
    pickle_file_path = os.path.join(output_folder, 'face_decodificada.pickle')

    # Salvar as informações em um arquivo pickle
    data_to_save = {
        'all_face_encodings': all_face_encodings,
        'all_face_names': all_face_names,
    }

    with open(pickle_file_path, 'wb') as file:
        pickle.dump(data_to_save, file)

    # Carregar as informações do arquivo
    def load_face_encodings(pickle_file_path):
        try:
            with open(pickle_file_path, 'rb') as file:
                data_loaded = pickle.load(file)
                return data_loaded
        except FileNotFoundError:
            # Se o arquivo não existir, retorne None
            return None

    # Carregar as informações do arquivo
    loaded_data = load_face_encodings(pickle_file_path)

    #informações carregadas
    if loaded_data:
        print(f"\nFotos Alunos: {scanned_aluno}")
        print(f"\nFotos Funcionarios: {scanned_funcionario}")
        print(f"\nFotos Bloqueados: {scanned_bloqueado}")
        print(f"\nTotal de Fotos Escaneadas: {scanned_aluno + scanned_funcionario + scanned_bloqueado}")
        
        print("\n\nTotal de Face Decodificadas:", len(loaded_data['all_face_encodings']))
        print("\nTotal de Nomes Encontrados:", len(loaded_data['all_face_names']))
        
        print(f"\n\nFotos Não Reconhecidas\n alunos: {unrecognized_aluno}\nFuncionários{unrecognized_funcionario}\nBloqueados{unrecognized_bloqueado}")
        
    else:
        print("Arquivo .pickle não encontrado.")

     
    return redirect('index')


