
# import cv2
# import face_recognition
# import os
# import numpy as np
# import pickle
# import dlib
# from multiprocessing import Pool

# # Carregar o modelo de marcos faciais do dlib
# predictor = dlib.shape_predictor("modelo_deteccao/shape_predictor_81_face_landmarks.dat")

# # Função para determinar a cor de texto com melhor contraste (branco ou preto)
# def choose_text_color(average_color):
#     # Calcula a luminância da cor (brilho)
#     luminance = (0.299 * average_color[2] + 0.587 * average_color[1] + 0.114 * average_color[0])

#     # Escolhe a cor do texto com base na luminância
#     if luminance > 127:
#         return (0, 0, 0)  # Texto preto para fundos claros
#     else:
#         return (255, 255, 255)  # Texto branco para fundos escuros

# # Função para processar um quadro
# def process_frame(frame):
#     # Encontrar todas as faces no quadro
#     face_locations = face_recognition.face_locations(frame)
#     face_encodings = face_recognition.face_encodings(frame, face_locations)

#     # Inicializar uma lista para armazenar as posições verticais de todas as faces
#     vertical_positions = []

#     # Loop sobre as faces encontradas
#     for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
#         # Calcular a posição vertical média da face atual
#         vertical_position = (top + bottom) // 2
#         vertical_positions.append(vertical_position)

#         # Desenhar um retângulo ao redor da face
#         cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

#     # Calcular a posição vertical média de todas as faces
#     if vertical_positions:
#         average_vertical_position = sum(vertical_positions) // len(vertical_positions)
#     else:
#         # Caso não haja faces detectadas, use uma posição padrão
#         average_vertical_position = 100  # Ajuste para a posição desejada

#     # Definir o limite de similaridade (ajuste conforme necessário)
#     threshold = 0.48

#    # Loop sobre as faces encontradas
#     for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
#         # Calcular a distância entre a face atual e as faces conhecidas
#         face_distances = face_recognition.face_distance(all_face_encodings, face_encoding)

#         # Verificar se alguma das distâncias está abaixo do limite de similaridade
#         matches = [os.path.basename(name) for i, name in enumerate(all_face_names) if face_distances[i] < threshold]

#         if matches:
#             name = matches[0]  # Usar apenas o primeiro nome da lista de correspondências
#         else:
#             name = "Desconhecido"

#         # Determine a média de cor na região onde o texto será exibido
#         roi = frame[top:bottom, left:right]
#         average_color = np.mean(roi, axis=(0, 1))

#         # Escolha a cor do texto com melhor contraste
#         text_color = choose_text_color(average_color)

#         # Calcular a largura do texto
#         font = cv2.FONT_HERSHEY_DUPLEX
#         text_size = cv2.getTextSize(name, font, 0.5, 1)[0]
#         text_width = text_size[0]

#         # Definir a posição para desenhar o nome centralizado
#         text_x = left + (right - left - text_width) // 2
#         text_y = average_vertical_position - 10  # Ajuste o valor -10 conforme necessário

#         # Determinar a cor da borda de detecção com base na classe
#         if "estudante" in name:
#             border_color = (255, 0, 0)  # Azul para estudantes
#         elif "funcionario" in name:
#             border_color = (0, 255, 255)  # Amarelo para funcionários
#         elif "bloqueado" in name:
#             border_color = (0, 0, 255)  # Vermelho para bloqueados
#         else:
#             border_color = (0, 255, 0)  # Verde para desconhecidos

#         # Desenhar um retângulo ao redor da face com a cor determinada
#         cv2.rectangle(frame, (left, top), (right, bottom), border_color, 2)
#         text_y = bottom + 30   # Ajuste para a distância entre o retângulo e o nome

#         # Desenhar o nome centralizado
#         cv2.putText(frame, name, (text_x, text_y), font, 0.5, text_color, 1)
        
#     return frame


# # Função para carregar as informações do arquivo pickle
# def load_face_encodings(pickle_file_path):
#     try:
#         with open(pickle_file_path, 'rb') as file:
#             data_loaded = pickle.load(file)
#             return data_loaded
#     except FileNotFoundError:
#         # Se o arquivo não existir, retorne None
#         return None

# # Carregar as informações do arquivo pickle
# pickle_file_path = 'output/face_decodificada.pickle'
# loaded_data = load_face_encodings(pickle_file_path)

# if loaded_data:
#     # Extrair informações do arquivo pickle
#     all_face_encodings = loaded_data.get('all_face_encodings', [])
#     all_face_names = loaded_data.get('all_face_names', [])

    
#     # Definir o limite de similaridade (ajuste conforme necessário)/ 
#     # O valor do threshold é o limite que determina o que é "muito parecido" e o que é "muito diferente". 
#     # Se você definir o threshold para 0,5, isso significa que se a semelhança for maior que 0,5 (ou 50%), o sistema dirá que a pessoa é alguém que você conhece. 
#     # Se for menor que 0,5, o sistema dirá que a pessoa é "Desconhecida".
#     threshold = 0.48


#     # Inicializando a leitura do vídeo a partir de um arquivo de video
#     video_capture = cv2.VideoCapture('Video_teste/videoplayback(2).mp4')  # Substitua 'seuarquivo.mp4' pelo caminho do seu arquivo MP4
#     video_capture.set(cv2.CAP_PROP_FPS, 60)  # Altere o valor para a taxa de quadros desejada, por exemplo, 60 FPS

#     # Criando um pool de processos para paralelizar o processamento
#     num_processes = 4  # Ajuste conforme o número de nucleos do processador
#     pool = Pool(processes=num_processes)

#     while True:
#         ret, frame = video_capture.read()

#         if not ret:
#             break

#         # Dividindo os quadros em partes iguais para processamento paralelo
#         frames = np.array_split(frame, num_processes)

#         # Processando os quadros em paralelo
#         processed_frames = pool.map(process_frame, frames)

#         # Combine os quadros processados de volta em um único quadro
#         combined_frame = np.vstack(processed_frames)

#         # Mostrar o resultado
#         cv2.imshow('Reconhecimento Facial', combined_frame)

#         # Parar o programa pressionando a tecla 'q'
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # Fechar a janela
#     video_capture.release()
#     cv2.destroyAllWindows()
# else:
#     print("Arquivo pickle não encontrado.")






# import cv2
# import face_recognition
# import os
# import numpy as np
# import pickle
# import dlib
# from multiprocessing import Pool

# # Carregar o modelo de marcos faciais do dlib
# predictor = dlib.shape_predictor("modelo_deteccao/shape_predictor_81_face_landmarks.dat")

# # Função para determinar a cor de texto com melhor contraste (branco ou preto)
# def choose_text_color(average_color):
#     # Calcula a luminância da cor (brilho)
#     luminance = (0.299 * average_color[2] + 0.587 * average_color[1] + 0.114 * average_color[0])

#     # Escolhe a cor do texto com base na luminância
#     if luminance > 127:
#         return (0, 0, 0)  # Texto preto para fundos claros
#     else:
#         return (255, 255, 255)  # Texto branco para fundos escuros

# # Função para processar um quadro
# def process_frame(frame):
#     # Encontrar todas as faces no quadro
#     face_locations = face_recognition.face_locations(frame)
#     face_encodings = face_recognition.face_encodings(frame, face_locations)

#     # Loop sobre as faces encontradas
#     for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
#         # Calcular a distância entre a face atual e as faces conhecidas
#         face_distances = face_recognition.face_distance(all_face_encodings, face_encoding)

#         # Verificar se alguma das distâncias está abaixo do limite de similaridade
#         matches = [os.path.basename(name) for i, name in enumerate(all_face_names) if face_distances[i] < threshold]

#         if matches:
#             name = matches[0]  # Usar apenas o primeiro nome da lista de correspondências
#         else:
#             name = "Desconhecido"

#         # Determine a média de cor na região onde o texto será exibido
#         roi = frame[top:bottom, left:right]
#         average_color = np.mean(roi, axis=(0, 1))

#         # Escolha a cor do texto com melhor contraste
#         text_color = choose_text_color(average_color)

#         # Determinar a cor da borda de detecção com base na classe
#         if "estudante" in name:
#             border_color = (255, 0, 0)  # Azul para estudantes
#         elif "funcionario" in name:
#             border_color = (0, 255, 255)  # Amarelo para funcionários
#         elif "bloqueado" in name:
#             border_color = (0, 0, 255)  # Vermelho para bloqueados
#         else:
#             border_color = (0, 255, 0)  # Verde para desconhecidos

#         # Desenhar um retângulo ao redor da face e o nome com a cor determinada
#         cv2.rectangle(frame, (left, top), (right, bottom), border_color, 2)
#         font = cv2.FONT_HERSHEY_DUPLEX
#         cv2.putText(frame, name, (left + 6, bottom - 60), font, 0.5, text_color, 1)

#     return frame

# # Função para carregar as informações do arquivo pickle
# def load_face_encodings(pickle_file_path):
#     try:
#         with open(pickle_file_path, 'rb') as file:
#             data_loaded = pickle.load(file)
#             return data_loaded
#     except FileNotFoundError:
#         # Se o arquivo não existir, retorne None
#         return None

# # Carregar as informações do arquivo pickle
# pickle_file_path = 'output/face_decodificada.pickle'
# loaded_data = load_face_encodings(pickle_file_path)

# if loaded_data:
#     # Extrair informações do arquivo pickle
#     all_face_encodings = loaded_data.get('all_face_encodings', [])
#     all_face_names = loaded_data.get('all_face_names', [])

    
#     # Definir o limite de similaridade (ajuste conforme necessário)/ 
#     # O valor do threshold é o limite que determina o que é "muito parecido" e o que é "muito diferente". 
#     # Se você definir o threshold para 0,5, isso significa que se a semelhança for maior que 0,5 (ou 50%), o sistema dirá que a pessoa é alguém que você conhece. 
#     # Se for menor que 0,5, o sistema dirá que a pessoa é "Desconhecida".
#     threshold = 0.48


#     # Inicializando a leitura do vídeo a partir de um arquivo de video
#     video_capture = cv2.VideoCapture('videoplayback(2).mp4')  # Substitua 'seuarquivo.mp4' pelo caminho do seu arquivo MP4
#     video_capture.set(cv2.CAP_PROP_FPS, 60)  # Altere o valor para a taxa de quadros desejada, por exemplo, 60 FPS

#     # Criando um pool de processos para paralelizar o processamento
#     num_processes = 4  # Ajuste conforme o número de nucleos do processador
#     pool = Pool(processes=num_processes)

#     while True:
#         ret, frame = video_capture.read()

#         if not ret:
#             break

#         # Dividindo os quadros em partes iguais para processamento paralelo
#         frames = np.array_split(frame, num_processes)

#         # Processando os quadros em paralelo
#         processed_frames = pool.map(process_frame, frames)

#         # Combine os quadros processados de volta em um único quadro
#         combined_frame = np.vstack(processed_frames)

#         # Mostrar o resultado
#         cv2.imshow('Reconhecimento Facial', combined_frame)

#         # Parar o programa pressionando a tecla 'q'
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # Fechar a janela
#     video_capture.release()
#     cv2.destroyAllWindows()
# else:
#     print("Arquivo pickle não encontrado.")







# import cv2
# import face_recognition
# import os
# import numpy as np
# import pickle
# import dlib
# from multiprocessing import Pool

# # Função para determinar a cor de texto com melhor contraste (branco ou preto)
# def choose_text_color(average_color):
#     # Calcula a luminância da cor (brilho)
#     luminance = (0.299 * average_color[2] + 0.587 * average_color[1] + 0.114 * average_color[0])

#     # Escolhe a cor do texto com base na luminância
#     if luminance > 127:
#         return (0, 0, 0)  # Texto preto para fundos claros
#     else:
#         return (255, 255, 255)  # Texto branco para fundos escuros

# # Função para processar um quadro
# def process_frame(frame):
#     # Encontrar todas as faces no quadro
#     face_locations = face_recognition.face_locations(frame)
#     face_encodings = face_recognition.face_encodings(frame, face_locations)

#     # Inicializar uma lista para armazenar as posições verticais de todas as faces
#     vertical_positions = []

#     # Loop sobre as faces encontradas
#     for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
#         # Calcular a posição vertical média da face atual
#         vertical_position = (top + bottom) // 2
#         vertical_positions.append(vertical_position)

#         # Desenhar um retângulo ao redor da face
#         cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

#     # Calcular a posição vertical média de todas as faces
#     if vertical_positions:
#         average_vertical_position = sum(vertical_positions) // len(vertical_positions)
#     else:
#         # Caso não haja faces detectadas, use uma posição padrão
#         average_vertical_position = 100  # Ajuste para a posição desejada

#     # Definir o limite de similaridade (ajuste conforme necessário)
#     threshold = 0.48

#     # Loop sobre as faces encontradas
#     for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
#         # Calcular a distância entre a face atual e as faces conhecidas
#         face_distances = face_recognition.face_distance(all_face_encodings, face_encoding)

#         # Verificar se alguma das distâncias está abaixo do limite de similaridade
#         matches = [os.path.basename(name) for i, name in enumerate(all_face_names) if face_distances[i] < threshold]

#         if matches:
#             name = matches[0]  # Usar apenas o primeiro nome da lista de correspondências
#         else:
#             name = "Desconhecido"

#         # Determine a média de cor na região onde o texto será exibido
#         roi = frame[top:bottom, left:right]
#         average_color = np.mean(roi, axis=(0, 1))

#         # Escolha a cor do texto com melhor contraste
#         text_color = choose_text_color(average_color)

#         # Calcular a largura do texto
#         font = cv2.FONT_HERSHEY_DUPLEX
#         text_size = cv2.getTextSize(name, font, 0.8, 1)[0]
#         text_width = text_size[0]

#         # Definir a posição para desenhar o nome centralizado
#         text_x = left + (right - left - text_width) // 2
#         text_y = average_vertical_position - 10  # Ajuste o valor -10 conforme necessário

#         # Determinar a cor da borda de detecção com base na classe
#         if "estudante" in name:
#             border_color = (255, 0, 0)  # Azul para estudantes
#         elif "funcionario" in name:
#             border_color = (0, 255, 255)  # Amarelo para funcionários
#         elif "bloqueado" in name:
#             border_color = (0, 0, 255)  # Vermelho para bloqueados
#         else:
#             border_color = (0, 255, 0)  # Verde para desconhecidos

#         # Desenhar um retângulo ao redor da face com a cor determinada
#         cv2.rectangle(frame, (left, top), (right, bottom), border_color, 3)
#         text_y = bottom + 30  # Ajuste para a distância entre o retângulo e o nome

#         # Desenhar o nome centralizado
#         cv2.putText(frame, name, (text_x, text_y), font, 0.8, text_color, 1)

#     return frame

# # Função para carregar as informações do arquivo pickle
# def load_face_encodings(pickle_file_path):
#     try:
#         with open(pickle_file_path, 'rb') as file:
#             data_loaded = pickle.load(file)
#             return data_loaded
#     except FileNotFoundError:
#         # Se o arquivo não existir, retorne None
#         return None

# # Carregar as informações do arquivo pickle
# pickle_file_path = 'output/face_decodificada.pickle'
# loaded_data = load_face_encodings(pickle_file_path)

# if loaded_data:
#     # Extrair informações do arquivo pickle
#     all_face_encodings = loaded_data.get('all_face_encodings', [])
#     all_face_names = loaded_data.get('all_face_names', [])

#     # Inicializando a leitura do vídeo a partir de um arquivo de vídeo
#     video_capture = cv2.VideoCapture('Video_teste/videoplayback (1).mp4')  # Substitua 'seuarquivo.mp4' pelo caminho do seu arquivo MP4
#     video_capture.set(cv2.CAP_PROP_FPS, 60)  # Altere o valor para a taxa de quadros desejada, por exemplo, 60 FPS

#     # Defina a janela para ser inicialmente em modo normal (não tela cheia)
#     cv2.namedWindow('Reconhecimento Facial', cv2.WINDOW_NORMAL)

#     # Criando um pool de processos para paralelizar o processamento
#     num_processes = 4  # Ajuste conforme o número de núcleos do processador
#     pool = Pool(processes=num_processes)

#     while True:
#         ret, frame = video_capture.read()

#         if not ret:
#             break

#         # Dividindo os quadros em partes iguais para processamento paralelo
#         frames = np.array_split(frame, num_processes)

#         # Processando os quadros em paralelo
#         processed_frames = pool.map(process_frame, frames)

#         # Combine os quadros processados de volta em um único quadro
#         combined_frame = np.vstack(processed_frames)

#         # Mostrar o resultado
#         cv2.imshow('Reconhecimento Facial', combined_frame)

#         # Detectar pressionamento de tecla
#         key = cv2.waitKey(1) & 0xFF

#         # Opção para alternar entre tela cheia e modo normal (pressionando 'F' ou 'f')
#         if key == ord('F') or key == ord('f'):
#             # Verifique o estado atual da janela e alterne entre tela cheia e modo normal
#             window_state = cv2.getWindowProperty('Reconhecimento Facial', cv2.WND_PROP_FULLSCREEN)
#             if window_state == cv2.WINDOW_NORMAL:
#                 cv2.setWindowProperty('Reconhecimento Facial', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
#             else:
#                 cv2.setWindowProperty('Reconhecimento Facial', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)

#         # Parar o programa pressionando a tecla 'q'
#         if key == ord('q'):
#             break

#     # Fechar a janela
#     video_capture.release()
#     cv2.destroyAllWindows()

# else:
#     print("Arquivo pickle não encontrado.")




# import cv2
# import face_recognition
# import os
# import numpy as np
# import pickle
# from concurrent.futures import ThreadPoolExecutor
# from screeninfo import get_monitors
# from sound.sound import play_alert

# # Variável global para controlar o modo de exibição
# fullscreen = False

# # Função para alternar entre tela cheia e janela normal
# def toggle_fullscreen():
#     global fullscreen
#     fullscreen = not fullscreen
#     if fullscreen:
#         cv2.setWindowProperty('Reconhecimento Facial', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
#     else:
#         cv2.setWindowProperty('Reconhecimento Facial', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)

# # Função para determinar a cor de texto com melhor contraste (branco ou preto)
# def choose_text_color(average_color):
#     # Calcula a luminância da cor (brilho)
#     luminance = (0.299 * average_color[2] + 0.587 * average_color[1] + 0.114 * average_color[0])

#     # Escolhe a cor do texto com base na luminância
#     if luminance > 127:
#         return (0, 0, 0)  # Texto preto para fundos claros
#     else:
#         return (255, 255, 255)  # Texto branco para fundos escuros

# # Função para carregar as informações do arquivo pickle
# def load_face_encodings(pickle_file_path):
#     try:
#         with open(pickle_file_path, 'rb') as file:
#             data_loaded = pickle.load(file)
#             return data_loaded
#     except FileNotFoundError:
#         # Se o arquivo não existir, retorne None
#         return None

# # Função para processar um quadro
# def process_frame(frame):
#     # Encontrar todas as faces no quadro
#     face_locations = face_recognition.face_locations(frame)
#     face_encodings = face_recognition.face_encodings(frame, face_locations)

#     # Inicializar uma lista para armazenar as posições verticais de todas as faces
#     vertical_positions = []

#     # Loop sobre as faces encontradas
#     for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
#         # Calcular a posição vertical média da face atual
#         vertical_position = (top + bottom) // 2
#         vertical_positions.append(vertical_position)

#         # Desenhar um retângulo ao redor da face
#         cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

#     # Calcular a posição vertical média de todas as faces
#     if vertical_positions:
#         average_vertical_position = sum(vertical_positions) // len(vertical_positions)
#     else:
#         # Caso não haja faces detectadas, use uma posição padrão
#         average_vertical_position = 100  # Ajuste para a posição desejada

#     # Definir o limite de similaridade (ajuste conforme necessário)
#     threshold = 0.48

#     # Loop sobre as faces encontradas
#     for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
#         # Calcular a distância entre a face atual e as faces conhecidas
#         face_distances = face_recognition.face_distance(all_face_encodings, face_encoding)

#         # Verificar se alguma das distâncias está abaixo do limite de similaridade
#         matches = [os.path.basename(name) for i, name in enumerate(all_face_names) if face_distances[i] < threshold]

#         if matches:
#             name = matches[0]  # Usar apenas o primeiro nome da lista de correspondências
#         else:
#             name = "Desconhecido"

#         # Determine a média de cor na região onde o texto será exibido
#         roi = frame[top:bottom, left:right]
#         average_color = np.mean(roi, axis=(0, 1))

#         # Escolha a cor do texto com melhor contraste
#         text_color = choose_text_color(average_color)

#         # Calcular a largura do texto
#         font = cv2.FONT_HERSHEY_DUPLEX
#         text_size = cv2.getTextSize(name, font, 0.8, 1)[0]
#         text_width = text_size[0]

#         # Definir a posição para desenhar o nome centralizado
#         text_x = left + (right - left - text_width) // 2
#         text_y = average_vertical_position - 10  # Ajuste o valor -10 conforme necessário

#         # Determinar a cor da borda de detecção com base na classe
#         if "estudante" in name:
#             border_color = (255, 0, 0)  # Azul para estudantes
#         elif "funcionario" in name:
#             border_color = (0, 255, 255)  # Amarelo para funcionários
#         elif "bloqueado" in name:
#             border_color = (0, 0, 255)  # Vermelho para bloqueados
#             if play_alert:
#                 play_alert('alerta.mp3')  # Emita o aviso sonoro quando um rosto bloqueado for detectado
#         else:
#             border_color = (0, 255, 0)  # Verde para desconhecidos

#         # Desenhar um retângulo ao redor da face com a cor determinada
#         cv2.rectangle(frame, (left, top), (right, bottom), border_color, 3)
#         text_y = bottom + 30   # Ajuste para a distância entre o retângulo e o nome

#         # Desenhar o nome centralizado
#         cv2.putText(frame, name, (text_x, text_y), font, 0.8, text_color, 1, 5)

#     return frame

# if __name__ == "__main__":
#     # Carregar as informações do arquivo pickle
#     pickle_file_path = 'output/face_decodificada.pickle'
#     loaded_data = load_face_encodings(pickle_file_path)

#     if loaded_data:
#         # Extrair informações do arquivo pickle
#         all_face_encodings = loaded_data.get('all_face_encodings', [])
#         all_face_names = loaded_data.get('all_face_names', [])

#         # Inicializar a leitura do vídeo MP4
#         video_file_path = 'Video_teste/videoplayback.webm'  # Substitua pelo caminho do seu vídeo
#         video_capture = cv2.VideoCapture(video_file_path)

#         # Obter as dimensões do vídeo
#         video_width = int(video_capture.get(3))
#         video_height = int(video_capture.get(4))

#         # Configurar a janela OpenCV para as dimensões do vídeo
#         cv2.namedWindow('Reconhecimento Facial', cv2.WINDOW_NORMAL)
#         cv2.resizeWindow('Reconhecimento Facial', video_width, video_height)

#         # Crie um executor de thread para paralelizar o processamento dos quadros
#         with ThreadPoolExecutor(max_workers=4) as executor:
#             while True:
#                 # Capturar um quadro do vídeo MP4
#                 ret, frame = video_capture.read()

#                 if not ret:
#                     break  # Sai do loop quando o vídeo terminar

#                 # Processar o quadro usando o executor
#                 processed_frame = executor.submit(process_frame, frame).result()

#                 # Mostrar o resultado
#                 cv2.imshow('Reconhecimento Facial', processed_frame)

#                 # Detectar pressionamento da tecla 'x' para parar a reprodução do som
#                 key = cv2.waitKey(1) & 0xFF
#                 if key == ord('x'):
#                     if is_alert_playing:
#                         play_alert.stop()
#                         is_alert_playing = False
#                 if key == ord('q'):
#                     break
#                 elif key == ord('F') or key == ord('f'):
#                     toggle_fullscreen()

#         # Liberar recursos
#         video_capture.release()
#         cv2.destroyAllWindows()
#     else:
#         print("Arquivo pickle não encontrado.")




# import cv2
# import face_recognition
# import os
# import numpy as np
# import pickle
# import threading
# from screeninfo import get_monitors
# from sound.sound import play_alert

# # Variável global para controlar o modo de exibição
# fullscreen = False

# # Função para alternar entre tela cheia e janela normal
# def toggle_fullscreen():
#     global fullscreen
#     fullscreen = not fullscreen
#     if fullscreen:
#         cv2.setWindowProperty('Reconhecimento Facial', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
#     else:
#         cv2.setWindowProperty('Reconhecimento Facial', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)

# # Função para determinar a cor de texto com melhor contraste (branco ou preto)
# def choose_text_color(average_color):
#     # Calcula a luminância da cor (brilho)
#     luminance = (0.299 * average_color[2] + 0.587 * average_color[1] + 0.114 * average_color[0])

#     # Escolhe a cor do texto com base na luminância
#     if luminance > 127:
#         return (0, 0, 0)  # Texto preto para fundos claros
#     else:
#         return (255, 255, 255)  # Texto branco para fundos escuros

# # Função para carregar as informações do arquivo pickle
# def load_face_encodings(pickle_file_path):
#     try:
#         with open(pickle_file_path, 'rb') as file:
#             data_loaded = pickle.load(file)
#             return data_loaded
#     except FileNotFoundError:
#         # Se o arquivo não existir, retorne None
#         return None

# # Função para processar um quadro
# def process_frame(frame):
#     # Encontrar todas as faces no quadro
#     face_locations = face_recognition.face_locations(frame)
#     face_encodings = face_recognition.face_encodings(frame, face_locations)

#     # Inicializar uma lista para armazenar as posições verticais de todas as faces
#     vertical_positions = []

#     # Loop sobre as faces encontradas
#     for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
#         # Calcular a posição vertical média da face atual
#         vertical_position = (top + bottom) // 2
#         vertical_positions.append(vertical_position)

#         # Desenhar um retângulo ao redor da face
#         cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

#     # Calcular a posição vertical média de todas as faces
#     if vertical_positions:
#         average_vertical_position = sum(vertical_positions) // len(vertical_positions)
#     else:
#         # Caso não haja faces detectadas, use uma posição padrão
#         average_vertical_position = 100  # Ajuste para a posição desejada

#     # Definir o limite de similaridade (ajuste conforme necessário)
#     threshold = 0.48

#     # Loop sobre as faces encontradas
#     for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
#         # Calcular a distância entre a face atual e as faces conhecidas
#         face_distances = face_recognition.face_distance(all_face_encodings, face_encoding)

#         # Verificar se alguma das distâncias está abaixo do limite de similaridade
#         matches = [os.path.basename(name) for i, name in enumerate(all_face_names) if face_distances[i] < threshold]

#         if matches:
#             name = matches[0]  # Usar apenas o primeiro nome da lista de correspondências
#         else:
#             name = "Desconhecido"

#         # Determine a média de cor na região onde o texto será exibido
#         roi = frame[top:bottom, left:right]
#         average_color = np.mean(roi, axis=(0, 1))

#         # Escolha a cor do texto com melhor contraste
#         text_color = choose_text_color(average_color)

#         # Calcular a largura do texto
#         font = cv2.FONT_HERSHEY_DUPLEX
#         text_size = cv2.getTextSize(name, font, 0.8, 1)[0]
#         text_width = text_size[0]

#         # Definir a posição para desenhar o nome centralizado
#         text_x = left + (right - left - text_width) // 2
#         text_y = average_vertical_position - 10  # Ajuste o valor -10 conforme necessário

#         # Determinar a cor da borda de detecção com base na classe
#         if "estudante" in name:
#             border_color = (255, 0, 0)  # Azul para estudantes
#         elif "funcionario" in name:
#             border_color = (0, 255, 255)  # Amarelo para funcionários
#         elif "bloqueado" in name:
#             border_color = (0, 0, 255)  # Vermelho para bloqueados
#             if play_alert:
#                 play_alert('sound/alerta.mp3')  # Emita o aviso sonoro quando um rosto bloqueado for detectado
#         else:
#             border_color = (0, 255, 0)  # Verde para desconhecidos

#         # Desenhar um retângulo ao redor da face com a cor determinada
#         cv2.rectangle(frame, (left, top), (right, bottom), border_color, 3)
#         text_y = bottom + 30   # Ajuste para a distância entre o retângulo e o nome

#         # Desenhar o nome centralizado
#         cv2.putText(frame, name, (text_x, text_y), font, 0.8, text_color, 1, 5)

#     return frame

# # Função para reproduzir um alerta sonoro em uma thread separada
# def play_alert_sound_thread(sound_file):
#     try:
#         play_alert(sound_file)
#     except Exception as e:
#         print("Erro ao reproduzir o alerta sonoro:", str(e))

# if __name__ == "__main__":
#     # Carregar as informações do arquivo pickle
#     pickle_file_path = 'output/face_decodificada.pickle'
#     loaded_data = load_face_encodings(pickle_file_path)

#     if loaded_data:
#         # Extrair informações do arquivo pickle
#         all_face_encodings = loaded_data.get('all_face_encodings', [])
#         all_face_names = loaded_data.get('all_face_names', [])

#         # Inicializar o leitor de vídeo a partir de um arquivo MP4
#         video_file_path = 'Video_teste/videoplayback.webm'
#         video_capture = cv2.VideoCapture(video_file_path)

#         # Obter as dimensões da tela real
#         monitors = get_monitors()
#         if monitors:
#             monitor = monitors[0]  # Use o primeiro monitor encontrado
#             screen_width = monitor.width
#             screen_height = monitor.height

#             # Configurar a janela OpenCV para as dimensões da tela real
#             cv2.namedWindow('Reconhecimento Facial', cv2.WINDOW_NORMAL)
#             cv2.resizeWindow('Reconhecimento Facial', screen_width, screen_height)

#         # Criar uma thread para reproduzir o som de alerta
#         alert_thread = threading.Thread(target=play_alert_sound_thread, args=('sound/alerta.mp3',))
#         alert_thread.daemon = True
#         alert_thread.start()

#         while True:
#             # Capturar um quadro do vídeo
#             ret, frame = video_capture.read()

#             if not ret:
#                 break

#             # Processar o quadro
#             processed_frame = process_frame(frame)

#             # Mostrar o resultado
#             cv2.imshow('Reconhecimento Facial', processed_frame)

#             # Detectar pressionamento da tecla 'x' para parar a reprodução do som
#             key = cv2.waitKey(1) & 0xFF
#             if key == ord('x'):
#                 if is_alert_playing:
#                     alert_thread.join()
#                     is_alert_playing = False
#             if key == ord('q'):
#                 break
#             elif key == ord('F') or key == ord('f'):
#                 toggle_fullscreen()

#         # Liberar recursos
#         video_capture.release()
#         cv2.destroyAllWindows()
#     else:
#         print("Arquivo pickle não encontrado.")







# import cv2
# import face_recognition
# import os
# import numpy as np
# import pickle
# import threading
# from screeninfo import get_monitors
# from sound.sound import play_alert
# from multiprocessing import Process

# # Variável global para controlar o modo de exibição
# fullscreen = False
# is_alert_playing = False

# # Função para alternar entre tela cheia e janela normal
# def toggle_fullscreen():
#     global fullscreen
#     fullscreen = not fullscreen
#     if fullscreen:
#         cv2.setWindowProperty('Reconhecimento Facial', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
#     else:
#         cv2.setWindowProperty('Reconhecimento Facial', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)

# # Função para determinar a cor de texto com melhor contraste (branco ou preto)
# def choose_text_color(average_color):
#     # Calcula a luminância da cor (brilho)
#     luminance = (0.299 * average_color[2] + 0.587 * average_color[1] + 0.114 * average_color[0])

#     # Escolhe a cor do texto com base na luminância
#     if luminance > 127:
#         return (0, 0, 0)  # Texto preto para fundos claros
#     else:
#         return (255, 255, 255)  # Texto branco para fundos escuros

# # Função para carregar as informações do arquivo pickle
# def load_face_encodings(pickle_file_path):
#     try:
#         with open(pickle_file_path, 'rb') as file:
#             data_loaded = pickle.load(file)
#             return data_loaded
#     except FileNotFoundError:
#         # Se o arquivo não existir, retorne None
#         return None

# # Função para processar um quadro
# def process_frame(frame, all_face_encodings, all_face_names):
#     # Encontrar todas as faces no quadro
#     face_locations = face_recognition.face_locations(frame)
#     face_encodings = face_recognition.face_encodings(frame, face_locations)

#     # Inicializar uma lista para armazenar as posições verticais de todas as faces
#     vertical_positions = []

#     # Loop sobre as faces encontradas
#     for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
#         # Calcular a posição vertical média da face atual
#         vertical_position = (top + bottom) // 2
#         vertical_positions.append(vertical_position)

#         # Desenhar um retângulo ao redor da face
#         cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

#     # Calcular a posição vertical média de todas as faces
#     if vertical_positions:
#         average_vertical_position = sum(vertical_positions) // len(vertical_positions)
#     else:
#         # Caso não haja faces detectadas, use uma posição padrão
#         average_vertical_position = 100  # Ajuste para a posição desejada

#     # Definir o limite de similaridade (ajuste conforme necessário)
#     threshold = 0.48

#     # Loop sobre as faces encontradas
#     for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
#         # Calcular a distância entre a face atual e as faces conhecidas
#         face_distances = face_recognition.face_distance(all_face_encodings, face_encoding)

#         # Verificar se alguma das distâncias está abaixo do limite de similaridade
#         matches = [os.path.basename(name) for i, name in enumerate(all_face_names) if face_distances[i] < threshold]

#         if matches:
#             name = matches[0]  # Usar apenas o primeiro nome da lista de correspondências
#         else:
#             name = "Desconhecido"

#         # Determine a média de cor na região onde o texto será exibido
#         roi = frame[top:bottom, left:right]
#         average_color = np.mean(roi, axis=(0, 1))

#         # Escolha a cor do texto com melhor contraste
#         text_color = choose_text_color(average_color)

#         # Calcular a largura do texto
#         font = cv2.FONT_HERSHEY_DUPLEX
#         text_size = cv2.getTextSize(name, font, 0.8, 1)[0]
#         text_width = text_size[0]

#         # Definir a posição para desenhar o nome centralizado
#         text_x = left + (right - left - text_width) // 2
#         text_y = average_vertical_position - 10  # Ajuste o valor -10 conforme necessário

#         # Determinar a cor da borda de detecção com base na classe
#         if "estudante" in name:
#             border_color = (255, 0, 0)  # Azul para estudantes
#         elif "funcionario" in name:
#             border_color = (0, 255, 255)  # Amarelo para funcionários
#         elif "bloqueado" in name:
#             border_color = (0, 0, 255)  # Vermelho para bloqueados
#             if play_alert:
#                 play_alert('sound/alerta.mp3')  # Emita o aviso sonoro quando um rosto bloqueado for detectado
#         else:
#             border_color = (0, 255, 0)  # Verde para desconhecidos

#         # Desenhar um retângulo ao redor da face com a cor determinada
#         cv2.rectangle(frame, (left, top), (right, bottom), border_color, 3)
#         text_y = bottom + 30   # Ajuste para a distância entre o retângulo e o nome

#         # Desenhar o nome centralizado
#         cv2.putText(frame, name, (text_x, text_y), font, 0.8, text_color, 1, 5)

#     return frame

# # Função para reproduzir um alerta sonoro
# def play_alert_sound(sound_file):
#     try:
#         play_alert(sound_file)
#     except Exception as e:
#         print("Erro ao reproduzir o alerta sonoro:", str(e))

# def video_processing_thread(video_file_path, all_face_encodings, all_face_names):
#     # Inicializar o leitor de vídeo a partir de um arquivo MP4
#     video_capture = cv2.VideoCapture(video_file_path)

#     while True:
#         # Capturar um quadro do vídeo
#         ret, frame = video_capture.read()

#         if not ret:
#             break

#         # Processar o quadro
#         processed_frame = process_frame(frame, all_face_encodings, all_face_names)

#         # Mostrar o resultado
#         cv2.imshow('Reconhecimento Facial', processed_frame)

#         # Detectar pressionamento da tecla 'x' para parar a reprodução do som
#         key = cv2.waitKey(1) & 0xFF
#         if key == ord('x'):
#             if is_alert_playing:
#                 alert_thread.join()
#                 is_alert_playing = False
#         if key == ord('q'):
#             break
#         elif key == ord('F') or key == ord('f'):
#             toggle_fullscreen()

#     video_capture.release()
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     # Carregar as informações do arquivo pickle
#     pickle_file_path = 'output/face_decodificada.pickle'
#     loaded_data = load_face_encodings(pickle_file_path)

#     if loaded_data:
#         # Extrair informações do arquivo pickle
#         all_face_encodings = loaded_data.get('all_face_encodings', [])
#         all_face_names = loaded_data.get('all_face_names', [])

#         # Criar uma thread para reproduzir o som de alerta
#         alert_thread = threading.Thread(target=play_alert_sound, args=('sound/alerta.mp3',))
#         alert_thread.daemon = True
#         alert_thread.start()

#         video_thread = threading.Thread(target=video_processing_thread, args=('Video_teste/videoplayback.mp4', all_face_encodings, all_face_names))
#         video_thread.daemon = True
#         video_thread.start()

#         alert_thread.join()
#         video_thread.join()
#     else:
#         print("Arquivo pickle não encontrado.")




import cv2
import face_recognition
import os
import numpy as np
import pickle
from screeninfo import get_monitors
import serial
from serial.tools import list_ports
import time

# Variável global para controlar o modo de exibição
fullscreen = False
num_processes = 11  # Número de processos desejado

# Variáveis para o cálculo do FPS
frame_count = 0
start_time = time.time()
fps_text = "FPS: 0.00"  # Inicialmente, o valor do FPS é zero

# Variáveis para controlar o número de reconhecimentos consecutivos
consecutive_recognitions = 0
min_recognitions_threshold = 20

# Encontre a porta do Arduino automaticamente
def find_arduino_port():
    arduino_ports = [port.device for port in list_ports.comports() if 'ttyACM0' in port.description]
    if arduino_ports:
        return arduino_ports[0]
    return None

# Encontra a porta do Arduino
arduino_port = find_arduino_port()

if arduino_port:
    arduino = serial.Serial(arduino_port, 9600)

# Função para alternar entre tela cheia e janela normal
def toggle_fullscreen():
    global fullscreen
    fullscreen = not fullscreen
    if fullscreen:
        cv2.setWindowProperty('Reconhecimento Facial', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    else:
        cv2.setWindowProperty('Reconhecimento Facial', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)

# Função para determinar a cor de texto com melhor contraste (branco ou preto)
def choose_text_color(average_color):
    luminance = (0.299 * average_color[2] + 0.587 * average_color[1] + 0.114 * average_color[0])

    if luminance > 127:
        return (0, 0, 255)
    else:
        return (255, 255, 255)

# Função para carregar as informações do arquivo pickle
def load_face_encodings(pickle_file_path):
    try:
        with open(pickle_file_path, 'rb') as file:
            data_loaded = pickle.load(file)
            return data_loaded
    except FileNotFoundError:
        return None

# Função para processar um quadro
def process_frame(frame):
    global consecutive_recognitions  # Adicione esta linha

    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)
    vertical_positions = []

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        vertical_position = (top + bottom) // 2
        vertical_positions.append(vertical_position)
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    if vertical_positions:
        average_vertical_position = sum(vertical_positions) // len(vertical_positions)
    else:
        average_vertical_position = 100

    threshold = 0.45

    try:
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            face_distances = face_recognition.face_distance(all_face_encodings, face_encoding)
            matches = [os.path.basename(name) for i, name in enumerate(all_face_names) if face_distances[i] < threshold]

            if matches:
                name = matches[0]
                similarity_percentage = min((1.0 - face_distances[matches.index(name)]) / (1.0 - threshold) * 100, 100)
                text = f"{name} ({similarity_percentage:.2f}%)"
            else:
                name = "Desconhecido"
                text = name

            roi = frame[top:bottom, left:right]
            average_color = np.mean(roi, axis=(0, 1))
            text_color = choose_text_color(average_color)
            text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_DUPLEX, 0.8, 1)[0]
            text_width = text_size[0]
            text_x = left + (right - left - text_width) // 2
            text_y = bottom + 30

            if "Estudante" in name:
                border_color = (255, 0, 0)
                consecutive_recognitions += 1
                if consecutive_recognitions >= min_recognitions_threshold:
                    arduino.write(b'1')
            elif "Funcionario" in name:
                border_color = (0, 255, 255)
                consecutive_recognitions += 1
                if consecutive_recognitions >= min_recognitions_threshold:
                    arduino.write(b'1')
            elif "Bloqueado" in name:
                border_color = (0, 0, 255)
                arduino.write(b'3')  # Envia imediatamente o número 3 para o Arduino
                consecutive_recognitions = 0  # Reinicia o contador de reconhecimentos consecutivos
            else:
                border_color = (0, 255, 0)
                arduino.write(b'3')  # Envia imediatamente o número 3 para o Arduino
                consecutive_recognitions = 0  # Reinicia o contador de reconhecimentos consecutivos

            cv2.rectangle(frame, (left, top), (right, bottom), border_color, 3)
            text_y = bottom + 30
            cv2.putText(frame, text, (text_x, text_y), cv2.FONT_HERSHEY_DUPLEX, 0.8, text_color, 1, 5)

    except Exception as e:
        print(f"Erro: {e}")

    return frame

# Função para exibir o FPS
def display_fps(frame):
    global frame_count, start_time, fps_text
    frame_count += 1

    if time.time() - start_time >= 1:
        fps = frame_count / (time.time() - start_time)
        frame_count = 0
        start_time = time.time()
        fps_text = f"FPS: {fps:.2f}"

    cv2.putText(frame, fps_text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

if __name__ == "__main__":
    pickle_file_path = 'output/face_decodificada.pickle'
    loaded_data = load_face_encodings(pickle_file_path)

    if loaded_data:
        all_face_encodings = loaded_data.get('all_face_encodings', [])
        all_face_names = loaded_data.get('all_face_names', [])

        
        
        # Substitua a inicialização do objeto video_capture para ler de um arquivo de vídeo
        video_path = 'Video_teste/video1080p.mp4'
        video_capture = cv2.VideoCapture(video_path)
        
        
        
        desired_width = 640
        desired_height = 480
        desired_framerate = 30
        video_capture.set(3, desired_width)
        video_capture.set(4, desired_height)
        video_capture.set(5, desired_framerate)

        monitors = get_monitors()
        if monitors:
            monitor = monitors[0]
            screen_width = monitor.width
            screen_height = monitor.height
            cv2.namedWindow('Reconhecimento Facial', cv2.WINDOW_NORMAL)
            cv2.resizeWindow('Reconhecimento Facial', screen_width, screen_height)

        while True:
            ret, frame = video_capture.read()

            display_fps(frame)  # Chama a função para exibir o FPS

            processed_frame = process_frame(frame)

            cv2.imshow('Reconhecimento Facial', processed_frame)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('F') or key == ord('f'):
                toggle_fullscreen()

        video_capture.release()
        cv2.destroyAllWindows()
    else:
        print("Arquivo pickle não encontrado.")

