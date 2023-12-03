
# import pickle

# # Abra o arquivo pickle para leitura binária
# with open('output/face_decodificada.pickle', 'rb') as file:
#     # Carregue os dados do arquivo pickle
#     dados = pickle.load(file)

# # Use pickle.dumps para obter uma representação de string dos dados originais
# dados_em_string = pickle.dumps(dados)

# # Exiba a representação em string dos dados originais
# print("Dados no arquivo pickle (representação em string):\n\n\n")
# print(dados_em_string)









# Teste de identificação facial Opencv e face_recognition

# import cv2
# import face_recognition

# # Inicialize a captura de vídeo da webcam
# video_capture = cv2.VideoCapture(0)

# while True:
#     # Capturar um quadro da webcam
#     ret, frame = video_capture.read()

#     # Converter o quadro para RGB (necessário para face_recognition)
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     # Encontrar todas as localizações de rostos no quadro
#     face_locations = face_recognition.face_locations(rgb_frame)

#     # Para cada rosto encontrado, desenhe um retângulo e pontos faciais
#     for face_location in face_locations:
#         top, right, bottom, left = face_location

#         # Desenhe um retângulo ao redor do rosto
#         cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

#         # Encontrar pontos faciais do rosto
#         landmarks = face_recognition._raw_face_landmarks(rgb_frame, [face_location])
#         for landmark in landmarks:
#             for feature, points in landmark.items():
#                 for point in points:
#                     cv2.circle(frame, point, 2, (0, 255, 0), -1)

#     # Exibir o quadro resultante
#     cv2.imshow("Video", frame)

#     # Verifique se o usuário pressionou a tecla 'q' para sair
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Libere a captura de vídeo e feche a janela
# video_capture.release()
# cv2.destroyAllWindows()








# # Teste de identificação usando as Embeddings
# import cv2
# import face_recognition

# # Inicialize a webcam
# video_capture = cv2.VideoCapture(0)

# while True:
#     # Capture o quadro de vídeo
#     ret, frame = video_capture.read()

#     # Encontre todos os rostos na imagem
#     face_locations = face_recognition.face_locations(frame)
#     face_encodings = face_recognition.face_encodings(frame, face_locations)

#     for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
#         # Desenhe um retângulo ao redor do rosto
#         cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

#         # Exiba as embeddings na imagem
#         font = cv2.FONT_HERSHEY_DUPLEX
#         text = ", ".join(str(value) for value in face_encoding)
#         cv2.putText(frame, text, (left, top - 10), font, 0.5, (255, 255, 255), 1)

#     # Exiba o quadro de vídeo resultante
#     cv2.imshow("Video", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Libere a webcam e feche a janela
# video_capture.release()
# cv2.destroyAllWindows()



import serial
from serial.tools import list_ports

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
    
    try:
        while True:
            command = input("Digite '1' ou '0' (ou pressione Ctrl+C para encerrar): ")
            
            if command == '1':
                arduino.write(b'1')  # Envia '1' para o Arduino
            elif command == '0':
                arduino.write(b'0')  # Envia '0' para o Arduino
            elif command == '2':
                arduino.write(b'2')  # Envia '2' para o Arduino
    except KeyboardInterrupt:
        print("Encerrando o programa.")




# import PIL.Image
# import dlib
# import numpy as np
# from PIL import ImageFile
# import cv2

# try:
#     import face_recognition_models
# except Exception:
#     print("Por favor, instale `face_recognition_models` com este comando antes de usar `face_recognition`: \n")
#     print("pip install git+https://github.com/ageitgey/face_recognition_models")
#     quit()

# ImageFile.LOAD_TRUNCATED_IMAGES = True

# face_detector = dlib.get_frontal_face_detector()

# preditor_68_point_model = face_recognition_models.pose_predictor_model_location()
# pose_predictor_68_point = dlib.shape_predictor(preditor_68_point_model)

# preditor_5_point_model = face_recognition_models.pose_predictor_five_point_model_location()
# pose_predictor_5_point = dlib.shape_predictor(preditor_5_point_model)

# cnn_face_detection_model = face_recognition_models.cnn_face_detector_model_location()
# cnn_face_detector = dlib.cnn_face_detection_model_v1(cnn_face_detection_model)

# face_recognition_model = face_recognition_models.face_recognition_model_location()
# face_encoder = dlib.face_recognition_model_v1(face_recognition_model)


# def _rect_to_css(rect):
#     return rect.top(), rect.right(), rect.bottom(), rect.left()


# def _css_to_rect(css):
#     return dlib.rectangle(css[3], css[0], css[1], css[2])


# def _trim_css_to_bounds(css, image_shape):
#     return max(css[0], 0), min(css[1], image_shape[1]), min(css[2], image_shape[0]), max(css[3], 0)


# def face_distance(face_encodings, face_to_compare):
#     if len(face_encodings) == 0:
#         return np.empty((0,))
#     return np.linalg.norm(face_encodings - face_to_compare, axis=1)


# def load_image_file(file, mode='RGB'):
#     im = PIL.Image.open(file)
#     if mode:
#         im = im.convert(mode)
#     return np.array(im)


# def _raw_face_locations(img, number_of_times_to_upsample=1, model="hog"):
#     if model == "cnn":
#         return cnn_face_detector(img, number_of_times_to_upsample)
#     else:
#         return face_detector(img, number_of_times_to_upsample)


# def face_locations(img, number_of_times_to_upsample=1, model="hog"):
#     if model == "cnn":
#         return [_trim_css_to_bounds(_rect_to_css(face.rect), img.shape) for face in _raw_face_locations(img, number_of_times_to_upsample, "cnn")]
#     else:
#         return [_trim_css_to_bounds(_rect_to_css(face), img.shape) for face in _raw_face_locations(img, number_of_times_to_upsample, model)]


# def _raw_face_locations_batched(images, number_of_times_to_upsample=1, batch_size=128):
#     return cnn_face_detector(images, number_of_times_to_upsample, batch_size=batch_size)


# def batch_face_locations(images, number_of_times_to_upsample=1, batch_size=128):
#     def convert_cnn_detections_to_css(detections):
#         return [_trim_css_to_bounds(_rect_to_css(face.rect), images[0].shape) for face in detections]

#     raw_detections_batched = _raw_face_locations_batched(images, number_of_times_to_upsample, batch_size)

#     return list(map(convert_cnn_detections_to_css, raw_detections_batched))


# def _raw__raw_face_landmarks(face_image, face_locations=None, model="large"):
#     if face_locations is None:
#         face_locations = _raw_face_locations(face_image)
#     else:
#         face_locations = [_css_to_rect(face_location) for face_location in face_locations]

#     pose_predictor = pose_predictor_68_point

#     if model == "small":
#         pose_predictor = pose_predictor_5_point

#     return [pose_predictor(face_image, face_location) for face_location in face_locations]


# def _raw_face_landmarks(face_image, face_locations=None, model="large"):
#     landmarks = _raw__raw_face_landmarks(face_image, face_locations, model)
#     landmarks_as_tuples = [[(p.x, p.y) for p in landmark.parts()] for landmark in landmarks]

#     if model == 'large':
#         return [{
#             "chin": landmarks_points[0:17],
#             "sobrancelha esquerda": landmarks_points[17:22],
#             "sobrancelha direita": landmarks_points[22:27],
#             "ponte_nose": landmarks_points[27:31],
#             "ponta do nariz": landmarks_points[31:36],
#             "olho_esquerdo": landmarks_points[36:42],
#             "olho_direito": landmarks_points[42:48],
#             "lábio superior": landmarks_points[48:55] + [landmarks_points[64]] + [landmarks_points[63]] + [landmarks_points[62]] + [landmarks_points[61]] + [landmarks_points[60]],
#             "bottom_lip": landmarks_points[54:60] + [landmarks_points[48]] + [landmarks_points[60]] + [landmarks_points[67]] + [landmarks_points[66]] + [landmarks_points[65]] + [landmarks_points[64]]
#         } for landmarks_points in landmarks_as_tuples]
#     elif model == 'small':
#         return [{"nose_tip": [landmarks_points[4]], "left_eye": landmarks_points[2:4], "right_eye": landmarks_points[0:2]} for landmarks_points in landmarks_as_tuples]
#     else:
#         raise ValueError("Tipo de modelo de pontos de referência inválido. Os modelos suportados são ['small', 'large'].")


# def face_encodings(face_image, known_face_locations=None, num_jitters=1, model="small"):
#     raw_landmarks = _raw__raw_face_landmarks(face_image, known_face_locations, model)
#     return [np.array(face_encoder.compute_face_descriptor(face_image, raw_landmark_set, num_jitters)) for raw_landmark_set in raw_landmarks]


# def compare_faces(known_face_encodings, face_encoding_to_check, tolerance=0.6):
#     return list(face_distance(known_face_encodings, face_encoding_to_check) <= tolerance)


# # Captura de vídeo da webcam
# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()

#     # Verificar se o frame não está vazio
#     if not ret or frame is None:
#         continue

#     # Converter a imagem capturada para o formato correto (RGB)
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     # Detectar rostos na imagem
#     detected_faces = face_locations(rgb_frame, model="cnn")

#     # Desenhar retângulos ao redor dos rostos detectados
#     for top, right, bottom, left in detected_faces:
#         cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

#     # Exibir o resultado
#     cv2.imshow('Webcam Face Detection', frame)

#     # Sair do loop se a tecla 'q' for pressionada
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Liberar os recursos
# cap.release()
# cv2.destroyAllWindows()





# import cv2
# import face_recognition
# import os
# import numpy as np
# import pickle
# from screeninfo import get_monitors
# import serial
# from serial.tools import list_ports
# import time
# import dlib
# import face_recognition_models

# # Inicialização do detector facial e preditores
# face_detector = dlib.get_frontal_face_detector()

# preditor_68_point_model = face_recognition_models.pose_predictor_model_location()
# pose_predictor_68_point = dlib.shape_predictor(preditor_68_point_model)

# preditor_5_point_model = face_recognition_models.pose_predictor_five_point_model_location()
# pose_predictor_5_point = dlib.shape_predictor(preditor_5_point_model)

# cnn_face_detection_model = face_recognition_models.cnn_face_detector_model_location()
# cnn_face_detector = dlib.cnn_face_detection_model_v1(cnn_face_detection_model)

# face_recognition_model = face_recognition_models.face_recognition_model_location()
# face_encoder = dlib.face_recognition_model_v1(face_recognition_model)

# # Variável global para controlar o modo de exibição
# fullscreen = False
# num_processes = 12  # Número de processos desejado

# # Variáveis para o cálculo do FPS
# frame_count = 0
# start_time = time.time()
# fps_text = "FPS: 0.00"  # Inicialmente, o valor do FPS é zero

# # Encontre a porta do Arduino automaticamente
# def find_arduino_port():
#     arduino_ports = [port.device for port in list_ports.comports() if 'ttyACM0' in port.description]
#     if arduino_ports:
#         return arduino_ports[0]
#     return None

# # Encontra a porta do Arduino
# arduino_port = find_arduino_port()

# if arduino_port:
#     arduino = serial.Serial(arduino_port, 9600)

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
#     luminance = (0.299 * average_color[2] + 0.587 * average_color[1] + 0.114 * average_color[0])

#     if luminance > 127:
#         return (0, 0, 0)
#     else:
#         return (255, 255, 255)

# # Função para carregar as informações do arquivo pickle
# def load_face_encodings(pickle_file_path):
#     try:
#         with open(pickle_file_path, 'rb') as file:
#             data_loaded = pickle.load(file)
#             return data_loaded
#     except FileNotFoundError:
#         return None

# # Função para processar um quadro
# def process_frame(frame):
#     face_locations = face_recognition.face_locations(frame)
#     face_encodings = face_recognition.face_encodings(frame, face_locations)
#     vertical_positions = []

#     for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
#         vertical_position = (top + bottom) // 2
#         vertical_positions.append(vertical_position)
#         cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

#     if vertical_positions:
#         average_vertical_position = sum(vertical_positions) // len(vertical_positions)
#     else:
#         average_vertical_position = 100

#     threshold = 0.48

#     for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
#         face_distances = face_recognition.face_distance(all_face_encodings, face_encoding)
#         matches = [os.path.basename(name) for i, name in enumerate(all_face_names) if face_distances[i] < threshold]

#         if matches:
#             name = matches[0]
#             similarity_percentage = min((1.0 - face_distances[matches.index(name)]) / (1.0 - threshold) * 100, 100)
#             text = f"{name} ({similarity_percentage:.2f}%)"
#         else:
#             name = "Desconhecido"
#             text = name

#         roi = frame[top:bottom, left:right]
#         average_color = np.mean(roi, axis=(0, 1))
#         text_color = choose_text_color(average_color)
#         text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_DUPLEX, 0.8, 1)[0]
#         text_width = text_size[0]
#         text_x = left + (right - left - text_width) // 2
#         text_y = bottom + 30

#         if "Estudante" in name:
#             border_color = (255, 0, 0)
#             arduino.write(b'1')
#         elif "Funcionario" in name:
#             border_color = (0, 255, 255)
#             arduino.write(b'1')
#         elif "Bloqueado" in name:
#             border_color = (0, 0, 255)
#         else:
#             border_color = (0, 255, 0)

#         cv2.rectangle(frame, (left, top), (right, bottom), border_color, 3)
#         text_y = bottom + 30
#         cv2.putText(frame, text, (text_x, text_y), cv2.FONT_HERSHEY_DUPLEX, 0.8, text_color, 1, 5)

#     return frame

# # Função para exibir o FPS
# def display_fps(frame):
#     global frame_count, start_time, fps_text
#     frame_count += 1

#     if time.time() - start_time >= 1:
#         fps = frame_count / (time.time() - start_time)
#         frame_count = 0
#         start_time = time.time()
#         fps_text = f"FPS: {fps:.2f}"

#     cv2.putText(frame, fps_text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

# # Função para obter marcos faciais brutos
# def _raw_face_landmarks(face_image, face_locations=None, model="large"):
#     landmarks = _raw_face_landmarks(face_image, face_locations, model)
#     landmarks_as_tuples = [[(p.x, p.y) for p in landmark.parts()] for landmark in landmarks]

#     if model == 'large':
#         return [{
#             "chin": landmarks_points[0:17],
#             "sobrancelha esquerda": landmarks_points[17:22],
#             "sobrancelha direita": landmarks_points[22:27],
#             "ponte_nose": landmarks_points[27:31],
#             "ponta do nariz": landmarks_points[31:36],
#             "olho_esquerdo": landmarks_points[36:42],
#             "olho_direito": landmarks_points[42:48],
#             "lábio superior": landmarks_points[48:55] + [landmarks_points[64]] + [landmarks_points[63]] + [landmarks_points[62]] + [landmarks_points[61]] + [landmarks_points[60]],
#             "bottom_lip": landmarks_points[54:60] + [landmarks_points[48]] + [landmarks_points[60]] + [landmarks_points[67]] + [landmarks_points[66]] + [landmarks_points[65]] + [landmarks_points[64]]
#         } for landmarks_points in landmarks_as_tuples]
#     elif model == 'small':
#         # Sua implementação do modelo pequeno aqui
#         pass

# if __name__ == "__main__":
#     pickle_file_path = 'output/face_decodificada.pickle'
#     loaded_data = load_face_encodings(pickle_file_path)

#     if loaded_data:
#         all_face_encodings = loaded_data.get('all_face_encodings', [])
#         all_face_names = loaded_data.get('all_face_names', [])

#         video_capture = cv2.VideoCapture(0)
#         desired_width = 640
#         desired_height = 480
#         desired_framerate = 30
#         video_capture.set(3, desired_width)
#         video_capture.set(4, desired_height)
#         video_capture.set(5, desired_framerate)

#         monitors = get_monitors()
#         if monitors:
#             monitor = monitors[0]
#             screen_width = monitor.width
#             screen_height = monitor.height
#             cv2.namedWindow('Reconhecimento Facial', cv2.WINDOW_NORMAL)
#             cv2.resizeWindow('Reconhecimento Facial', screen_width, screen_height)

#         while True:
#             ret, frame = video_capture.read()

#             display_fps(frame)  # Chama a função para exibir o FPS

#             processed_frame = process_frame(frame)

#             cv2.imshow('Reconhecimento Facial', processed_frame)

#             key = cv2.waitKey(1) & 0xFF
#             if key == ord('q'):
#                 break
#             elif key == ord('F') or key == ord('f'):
#                 toggle_fullscreen()

#         video_capture.release()
#         cv2.destroyAllWindows()
#     else:
#         print("Arquivo pickle não encontrado.")






# import cv2
# import face_recognition
# import os
# import numpy as np
# import pickle
# from screeninfo import get_monitors
# import serial
# from serial.tools import list_ports
# import time

# # Variável global para controlar o modo de exibição
# fullscreen = False
# num_processes = 11  # Número de processos desejado

# # Variáveis para o cálculo do FPS
# frame_count = 0
# start_time = time.time()
# fps_text = "FPS: 0.00"  # Inicialmente, o valor do FPS é zero

# # Variável global para contar o número de '1' enviados ao Arduino em um segundo
# num_ones_sent = 0

# # Encontre a porta do Arduino automaticamente
# def find_arduino_port():
#     arduino_ports = [port.device for port in list_ports.comports() if 'ttyACM0' in port.description]
#     if arduino_ports:
#         return arduino_ports[0]
#     return None

# # Encontra a porta do Arduino
# arduino_port = find_arduino_port()

# if arduino_port:
#     arduino = serial.Serial(arduino_port, 9600)

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
#     luminance = (0.299 * average_color[2] + 0.587 * average_color[1] + 0.114 * average_color[0])

#     if luminance > 127:
#         return (0, 0, 255)
#     else:
#         return (255, 255, 255)

# # Função para carregar as informações do arquivo pickle
# def load_face_encodings(pickle_file_path):
#     try:
#         with open(pickle_file_path, 'rb') as file:
#             data_loaded = pickle.load(file)
#             return data_loaded
#     except FileNotFoundError:
#         return None

# # Função para exibir o número de '1' enviados ao Arduino em um segundo
# def display_ones_per_second():
#     global num_ones_sent, start_time
#     current_time = time.time()

#     if current_time - start_time >= 1:
#         ones_per_second = num_ones_sent
#         num_ones_sent = 0
#         start_time = current_time
#         print(f"Number of '1' sent in the last second: {ones_per_second}")

# # Função para processar um quadro
# def process_frame(frame):
#     global num_ones_sent
#     face_locations = face_recognition.face_locations(frame)
#     face_encodings = face_recognition.face_encodings(frame, face_locations)
#     vertical_positions = []

#     for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
#         vertical_position = (top + bottom) // 2
#         vertical_positions.append(vertical_position)
#         cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

#     if vertical_positions:
#         average_vertical_position = sum(vertical_positions) // len(vertical_positions)
#     else:
#         average_vertical_position = 100

#     threshold = 0.47

#     for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
#         face_distances = face_recognition.face_distance(all_face_encodings, face_encoding)
#         matches = [os.path.basename(name) for i, name in enumerate(all_face_names) if face_distances[i] < threshold]

#         if matches:
#             name = matches[0]
#             similarity_percentage = min((1.0 - face_distances[matches.index(name)]) / (1.0 - threshold) * 100, 100)
#             text = f"{name} ({similarity_percentage:.2f}%)"
#         else:
#             name = "Desconhecido"
#             text = name

#         roi = frame[top:bottom, left:right]
#         average_color = np.mean(roi, axis=(0, 1))
#         text_color = choose_text_color(average_color)
#         text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_DUPLEX, 0.8, 1)[0]
#         text_width = text_size[0]
#         text_x = left + (right - left - text_width) // 2
#         text_y = bottom + 30

#         if "Estudante" in name:
#             border_color = (255, 0, 0)
#             arduino.write(b'1')
#             num_ones_sent += 1
            
#         elif "Funcionario" in name:
#             border_color = (0, 255, 255)
#             arduino.write(b'1')
#             num_ones_sent += 1
            
#         elif "Bloqueado" in name:
#             border_color = (0, 0, 255)
#         else:
#             border_color = (0, 255, 0)

#         cv2.rectangle(frame, (left, top), (right, bottom), border_color, 3)
#         text_y = bottom + 30
#         cv2.putText(frame, text, (text_x, text_y), cv2.FONT_HERSHEY_DUPLEX, 0.8, text_color, 1, 5)

#     return frame

# # Função para exibir o FPS
# def display_fps(frame):
#     global frame_count, start_time, fps_text
#     frame_count += 1

#     if time.time() - start_time >= 1:
#         fps = frame_count / (time.time() - start_time)
#         frame_count = 0
#         start_time = time.time()
#         fps_text = f"FPS: {fps:.2f}"

#     cv2.putText(frame, fps_text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

# if __name__ == "__main__":
#     pickle_file_path = 'output/face_decodificada.pickle'
#     loaded_data = load_face_encodings(pickle_file_path)

#     if loaded_data:
#         all_face_encodings = loaded_data.get('all_face_encodings', [])
#         all_face_names = loaded_data.get('all_face_names', [])

#         video_capture = cv2.VideoCapture(0)
#         desired_width = 640
#         desired_height = 480
#         desired_framerate = 30
#         video_capture.set(3, desired_width)
#         video_capture.set(4, desired_height)
#         video_capture.set(5, desired_framerate)

#         monitors = get_monitors()
#         if monitors:
#             monitor = monitors[0]
#             screen_width = monitor.width
#             screen_height = monitor.height
#             cv2.namedWindow('Reconhecimento Facial', cv2.WINDOW_NORMAL)
#             cv2.resizeWindow('Reconhecimento Facial', screen_width, screen_height)

#         while True:
#             ret, frame = video_capture.read()

#             display_fps(frame)  # Chama a função para exibir o FPS

#             processed_frame = process_frame(frame)

#             cv2.imshow('Reconhecimento Facial', processed_frame)

#             display_ones_per_second()  # Chama a função para exibir o número de '1' enviados em um segundo

#             key = cv2.waitKey(1) & 0xFF
#             if key == ord('q'):
#                 break
#             elif key == ord('F') or key == ord('f'):
#                 toggle_fullscreen()

#         video_capture.release()
#         cv2.destroyAllWindows()
#     else:
#         print("Arquivo pickle não encontrado.")
