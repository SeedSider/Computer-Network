#!/usr/bin/python
from socket import *
import subprocess
import os

serverPort = 12029
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while 1:
    connectionSocket, addr = serverSocket.accept()
    command = connectionSocket.recv(1024)
    if command == "-h":
        infoProcess = subprocess.check_output("lscpu | grep 'Architecture\|Vendor\|Model name\|CPU MHz\|cache'", shell = True)
        connectionSocket.send(infoProcess)
        connectionSocket.close()
    elif command == "-m":
        infoProcess = subprocess.check_output("free -m | grep -v Swap", shell = True)
        connectionSocket.send(infoProcess)
        connectionSocket.close()
    elif command == "-s":
        infoProcess = subprocess.check_output("free -m | grep -v Mem", shell = True)
        connectionSocket.send(infoProcess)
        connectionSocket.close()
    elif command == "-st":
        infoProcess = subprocess.check_output("df -h", shell = True)
        connectionSocket.send(infoProcess)
        connectionSocket.close()
    elif command == "-c":
        response = os.system("ping -c 1 8.8.8.8")
        if response == 0:
            pingstatus = "Network status is Online"
        else:
            pingstatus = "Network status is Offline"
        connectionSocket.send(pingstatus)
        connectionSocket.close()
    elif command == "-a":
        connectionSocket.close()
    elif command == "--help":
        infoProcess = '''How to Run : ./client.py <Server IP Address> <Server Port> <Argument>

        COMMAND LIST
        ------------------
        -h    : Get hardware info
        -m    : Get physical memory info
        -s    : Get swap memory info
        -st   : Get storage info
        -c    : Get server connection info
        -a    : Get account log info
        '''
        connectionSocket.send(infoProcess)
        connectionSocket.close()
    else:
        infoProcess = "Command not found please type \".\client.py --help\" for more info."
        connectionSocket.send(infoProcess)
        connectionSocket.close()
