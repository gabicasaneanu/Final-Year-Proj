import nmap
from socket import *


LocalSocket = socket(AF_INET,SOCK_DGRAM)
LocalSocket.connect(("8.8.8.8",80))
LocalIP = LocalSocket.getsockname()[0]
LocalSocket.close()
nm = nmap.PortScanner()


def initialize():
    if nm.has_host:
        nmscanner()
    else:
        print("network unreachable pal")


def nmscanner(): 
    
    nm.scan(hosts=LocalIP+'/24', arguments= 'n -sP -PE -PA21,23,80,3389')
    hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
    
    for host, status in hosts_list:
        a = nm.scan(hosts = host, arguments = '-A -v -n -p- -sT -sV -O --osscan-limit --max-os-tries 1')
        print(a)

nmscanner()

      
    
    
