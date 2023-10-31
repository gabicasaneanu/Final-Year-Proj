import socket
import platform
import os

try:
    f = open("info.txt","x")
except:
    #file exists
    os.remove("info.txt")
finally:
    f = open("info.txt","a")


    
    
    
    
LocalSocket = socket(socket.AF_INET,socket.SOCK_DGRAM)
LocalSocket.connect(("8.8.8.8",80))
LocalIP = LocalSocket.getsockname()[0]
LocalSocket.close()

f.append("host_IP = " + LocalIP)

f.close()