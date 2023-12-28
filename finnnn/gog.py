import subprocess
import netifaces
import os
import nmap


def writeHostAddress():
    x = netifaces.interfaces()
    x.pop(0)
    
    addresses = []
    r = []

    for i in x:
        if '192' in netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr']:
            pass
        else:
            addresses.append(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
            
    
        
    return (addresses[0])
    


host = writeHostAddress()
print(netifaces.interfaces())
interface = input("input interface: ")
victim = input("input victim: ")

        



nm = nmap.PortScanner()
a = nm.scan(hosts=victim, arguments= '-v -n -p- -sT -O --osscan-limit --max-os-tries 1')
print(a)
    
