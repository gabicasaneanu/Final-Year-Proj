import subprocess
import netifaces
import os
import nmap
import json
import re
from itertools import chain
from pprint import pprint
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

        

tries = 3
for i in range(tries):
    try:
        nm = nmap.PortScanner()
        nmScan = nm.scan(hosts=victim, arguments= '-sV -T4')
    except:
        if i < tries - 1:
            continue
        else:
            raise Exception('nmap scan failed - host may to be up, check host       connectivity / IP (Run Again, nmap may fail on occasion')
    break


try:
    protos = nm[victim].all_protocols()    
    for proto in protos:
        ports = nm[victim][proto].keys()
        portx = list(ports)
except:
    print('nmap scan failed, try running again')
    quit()
    
       
    
   
Vars = []
Titles = []


a = list(nmScan.values())
x = a[1]
for ports in portx:
    Vars.append([x[victim]['tcp'][ports]['product']])
    Titles.append([x[victim]['tcp'][ports]['version']])

varsx = list(chain.from_iterable(Vars))    
varsxx = list(filter(None,varsx))



    
CVEs = {}
for i,x  in enumerate(varsxx):
    print('services found : ',x, 'version - ', Titles[i])
    output = subprocess.run(['sudo','searchsploit',x,'-j'], capture_output = True).stdout
    logput = json.loads(output)
    pogput = list(logput.values())
    titles = pogput[2]
    somde = titles[-7:]
    for som in somde:
        print(som['Title'],som['Codes'])
        CVEs[som['Title']] = som['Codes'] 
          
         
               




     
            


            
            



    
    

    
    
    
        
