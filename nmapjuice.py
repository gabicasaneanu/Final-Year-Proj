import subprocess
import netifaces
import os
import nmap
import json
import re
from pkg_resources import packaging
from pkg_resources import parse_version as version

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
victim = '10.10.11.233'

        



nm = nmap.PortScanner()
nmScan = nm.scan(hosts=victim, arguments= '-sV -T4')

protos = nm[victim].all_protocols()    
for proto in protos:
    ports = nm[victim][proto].keys()
    portx = list(ports)
    
       
    
   
Vars = {}
Titles = []


a = list(nmScan.values())
x = a[1]
for ports in portx:
    Vars[x[victim]['tcp'][ports]['product']] = x[victim]['tcp'][ports]['version']
    
print(Vars)
thispass = '' 
for i in Vars:
    if not i:
        continue
    gong = i.split()
    act = gong[0]
    if re.match("^[A-Za-z_-]+$",act):
        output = subprocess.run(['sudo','searchsploit',act,'-j'], capture_output = True).stdout
        logput = json.loads(output)
        pogput = list(logput.values())
        titles = pogput[2]
        versione = Vars[i].split()
        versionel = versione[0]
        print('\n','exploits for:',act,'-',versionel)
        for title in titles:
            TitleVers = title['Title']
            print(title['Title'],title['Path'])
            
           
                  
                
                    
                       
            
        
        








    


#pompem






     
            


            
            



    
    

    
    
    
        
