import subprocess
import netifaces
import os
import nmap
import pprint

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
#print netifaces.interfaces()
interface = 'tun0'
victim = '10.10.11.242'

        



nm = nmap.PortScanner()
nmScan = nm.scan(hosts=victim, arguments= '-sV -T4')

protos = nm[victim].all_protocols()    
for proto in protos:
    ports = nm[victim][proto].keys()
    portx = list(ports)
    
       
    
   
Vars = {}



a = list(nmScan.values())
x = a[1]
for ports in portx:
    Vars[x[victim]['tcp'][ports]['product']] = x[victim]['tcp'][ports]['version']


print (Vars)
