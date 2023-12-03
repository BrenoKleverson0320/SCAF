
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

