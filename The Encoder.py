import socket
import base64
import subprocess

# Адрес и порт сервера
server_address = ('62.173.140.174', 10002)

# Создаем сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Подключаемся к серверу
    client_socket.connect(server_address)

    while True:
        # Получаем зашифрованный текст от сервера
        encrypted_data = client_socket.recv(1024)

        if not encrypted_data:
            break

        # Декодируем полученные данные из Base64
        decoded_data = base64.b64decode(encrypted_data)

        # Выводим расшифрованный текст для пользователя
        print("Расшифрованный текст:", decoded_data.decode('utf-8'))

        # Отправляем ответ на сервер
        response = input("Введите ваш ответ: ")
        client_socket.send(response.encode('utf-8'))

finally:
    # Закрываем соединение с сервером
    client_socket.close()