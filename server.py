#!/usr/bin/python
from socket import *
import subprocess

serverPort = 12029
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
successConnection = []
failedConnection = []
print('The server is ready to receive')
print("Server port is " + str(serverPort))
while 1:
    connectionSocket, addr = serverSocket.accept()
    command = connectionSocket.recv(1024)
    if command == "-h":
        successConnection.append(addr[0] + ", " + str(addr[1]))
        infoProcess = subprocess.check_output("lscpu | grep 'Architecture\|Vendor\|Model name\|CPU MHz\|cache'", shell = True)
        connectionSocket.send(infoProcess)
        connectionSocket.close()
    elif command == "-m":
        successConnection.append(addr[0] + ", " + str(addr[1]))
        infoProcess = subprocess.check_output("free -m | grep -v Swap", shell = True)
        connectionSocket.send(infoProcess)
        connectionSocket.close()
    elif command == "-s":
        successConnection.append(addr[0] + ", " + str(addr[1]))
        infoProcess = subprocess.check_output("free -m | grep -v Mem", shell = True)
        connectionSocket.send(infoProcess)
        connectionSocket.close()
    elif command == "-st":
        successConnection.append(addr[0] + ", " + str(addr[1]))
        infoProcess = subprocess.check_output("df -h", shell = True)
        connectionSocket.send(infoProcess)
        connectionSocket.close()
    elif command == "-c":
        successConnection.append(addr[0] + ", " + str(addr[1]))
        response = subprocess.call("ping -c 1 8.8.8.8", shell = True)
        if response == 0:
            pingstatus = "Network status is Online"
        else:
            pingstatus = "Network status is Offline"
        connectionSocket.send(pingstatus)
        connectionSocket.close()
    elif command == "-a":
        infoProcess = "Connected account log:"
        for x in successConnection:
            infoProcess += "\n" + x
        infoProcess += "\n\nFailed account log:"
        for y in failedConnection:
            infoProcess += "\n" + y
        connectionSocket.send(infoProcess)
        connectionSocket.close()
    elif command == "--help":
        infoProcess = '''How to Run : ./client.py <Server IP Address> <Server Port> <Command> or ./client.py <Command>
Please insert localhost as Server IP Address and 12029 as Server Port

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
        infoProcess = "Command not found. Please type \"./client.py --help\" for more info."
        failedConnection.append(addr[0] + ", " + str(addr[1]))
        connectionSocket.send(infoProcess)
        connectionSocket.close()
