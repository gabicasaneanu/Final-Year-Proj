import ipaddress
from socket import *
import os
from urllib import response
CommonPorts = [137,139,445,22,53,25,3389,80,443,8080,8443,20,21,23,1433,1434,3306]

#get local ip
LocalSocket = socket(AF_INET,SOCK_DGRAM)
LocalSocket.connect(("8.8.8.8",80))
LocalIP = LocalSocket.getsockname()[0]
LocalSocket.close()




#slow - Add Threads
def CommonPortScan():
    #scanning open ports
    Target = ("localhost")
    Target_IP = gethostbyname(Target)
    OpenPorts = []

    
    for Ports in range(len(CommonPorts)):
        OpenSocket = socket(AF_INET,SOCK_STREAM)
        SocketConnecter = OpenSocket.connect_ex((Target_IP,CommonPorts[Ports]))
        if (SocketConnecter == 0):
            OpenPorts.append(CommonPorts[Ports])
        OpenSocket.close()
    return (OpenPorts)

def PingSweep():
    
    IPrange = LocalIP.split(".")
    IPrange1 = IPrange[0] + "." + IPrange[1] + "." + IPrange[2] + "."
    for IPs in range(0,254):
        IPtemp =  IPrange1 + str(IPs)
        CMDresponse = os.popen("ping -n 1 " + IPtemp)
        for lines in CMDresponse.readlines():
            if(lines.count("TTL")):
                break
            if (lines.count("TTL")):
                print(IPtemp, "connectable")
            
def TCPSweep():
    OpenTCP = []
    IPrange = LocalIP.split(".")
    IPrange1 = IPrange[0] + "." + IPrange[1] + "." + IPrange[2] + "."
    
    for ip in range(0,254):
        
        OpenSocket = socket(AF_INET,SOCK_STREAM)
        OpenSocket.settimeout(1.0)
        ipaddress = IPrange1 + str(ip)
        print(1)
        result = OpenSocket.connect_ex((ipaddress,135))
        if result == 0:
            OpenTCP.append(ipaddress)
            print (1)
        else:
            OpenSocket.close()
    print(OpenTCP)

TCPSweep()
            
    
    
    
    
    

        
        
                 
    
    





    
        
        
        
    
