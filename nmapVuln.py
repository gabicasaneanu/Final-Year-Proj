import subprocess
import os
import nmap
import json
import sys
from itertools import chain


victim = sys.argv[1]

        

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
    print('nmap scan failed, check IP address')
    quit()
    
       
    
   
Vars = []
Titles = []


a = list(nmScan.values())
x = a[1]
try:
    for ports in portx:
        Vars.append([x[victim]['tcp'][ports]['product']])
        Titles.append([x[victim]['tcp'][ports]['version']])
except:
    print('nmap scan failed, check IP address')
    quit()

varsx = list(chain.from_iterable(Vars))    
varsxx = list(filter(None,varsx))



    
CVEs = {}
for i,x  in enumerate(varsxx):
    print('<b> services found : ',x, 'version - ', Titles[i],'</b>','<br/>')
    output = subprocess.run(['sudo','searchsploit',x,'-j'], capture_output = True).stdout
    logput = json.loads(output)
    pogput = list(logput.values())
    titles = pogput[2]
    somde = titles[-5:]
    for som in somde:
        print(som['Title'],som['Codes'],'<br/>')
        CVEs[som['Title']] = som['Codes'] 
          
         
               




     
            


            
            



    
    

    
    
    
        
