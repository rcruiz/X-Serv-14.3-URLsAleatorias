#!/usr/bin/python3

"""
Servidor de URLs Aleatorias
Rosa Cristina Ruiz Rivas
Alumna de SAT
"""

import socket
import random

# Crea un socket sobre TCP y se conecta a un determinado puerto
port = 1234
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', port))

# Podra escuchar hasta 5 conexiones TCP
mySocket.listen(5)

# Acepta las conexiones, lee datos entrantes y responde en una pagina HTML
try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('Request received:')
        print(recvSocket.recv(2048))
        # Genera las URLs aleatorias
        randomURL = str(random.randint(0, 1000000000))
        newURL = "http://localhost:" + str(port) + "/" + randomURL
        recvSocket.send(b"HTTP/1.1 200 OK\r\n\r\n" +
                        b"<html><body><p>Hola. " +
                        b'<a href="' + bytes(newURL, 'utf-8') + b'">' +
                        b"Dame otra </a></p></body></html>\r\n")
        recvSocket.close()
except KeyboardInterrupt:
    print("Closing binded socket")
    mySocket.close()
