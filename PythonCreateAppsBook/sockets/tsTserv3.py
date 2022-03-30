from socket import *
from time import time

HOST = '' #Любой доступный адрес
PORT = 21567 # рандомный порт
BUFSIZ = 1024 # размер бумера 1 кб
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET6, SOCK_STREAM) #вызов сокета сервера
tcpSerSock.bind(ADDR) #привязка к адресу
tcpSerSock.listen(5) #максимальное количество запросов на устн. соединения

while True: #запуск приемника запросов
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept() # принятие запроса на уст. соединения
    print('...connected from:', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ) # получения сообщеения TCP
        if not data:
            break
        tcpCliSock.send((str(time())+data.decode()).encode()) # отправка префика+ сообщения
    tcpCliSock.close()
tcpSerSock.close()