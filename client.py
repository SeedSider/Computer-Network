#!/usr/bin/python
from socket import *
import sys

serverName = 'localhost'
serverPort = 12029
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

command = sys.argv[-1]
clientSocket.send(command.encode('utf-8'))
recievedInfo = clientSocket.recv(1024)
print(recievedInfo)
clientSocket.close()
