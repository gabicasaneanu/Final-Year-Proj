from socket import *
import platform
import os





def initializer():
    
    
    LocalSocket = socket(AF_INET,SOCK_DGRAM)
    LocalSocket.connect(("8.8.8.8",80))
    LocalIP = LocalSocket.getsockname()[0]
    LocalSocket.close()
    
    operSystem = platform.system()
    print(operSystem)

    
    


initializer()